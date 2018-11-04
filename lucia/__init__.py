import pkg_resources

try:
    version = pkg_resources.get_distribution('lucia').version
except:
    version = 'dev'
