import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
#import email
import django

package = django
print("Path of module", package.__path__)
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    print ("Found submodule %s (is a package: %s)" % (modname, ispkg))