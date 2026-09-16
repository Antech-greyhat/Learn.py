# A script to proof that Tuple are immutable.
# you can tell a difference in the 2 variables the first one is a list while second is a Tuple.

mutable_config = ['ip_address', 'port', 'status']
mutable_config[0] = 'address'
mutable_config[2] = 'fail'
print(mutable_config) # output: ['address', 'port', 'fail']

mutable_config = ('ip_address', 'port', 'status')
mutable_config[1] = 'protocol' # TypeError: 'tuple' object does not support item assignment
mutable_config[2] = 'fail'   # TypeError: 'tuple' object does not support item assignment
print(mutable_config)

# TypeError prints because Tuple are Immutable once assigned cannot be changed.