# This file is generated by /private/var/folders/bb/n7t3rs157850byt_jfdcq9k80000gn/T/pip-sdt3rzj3-build/-c
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

blas_mkl_info={}
lapack_mkl_info={}
atlas_blas_info={}
lapack_opt_info={'extra_compile_args': ['-msse3'], 'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)]}
mkl_info={}
atlas_info={}
atlas_blas_threads_info={}
blas_opt_info={'extra_compile_args': ['-msse3', '-I/System/Library/Frameworks/vecLib.framework/Headers'], 'extra_link_args': ['-Wl,-framework', '-Wl,Accelerate'], 'define_macros': [('NO_ATLAS_INFO', 3)]}
atlas_threads_info={}
openblas_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    