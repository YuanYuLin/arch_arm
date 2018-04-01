import ops
import iopc

pkg_path = ""
output_dir = ""
arch_alt = ""

def set_global(args):
    global pkg_path 
    global output_dir
    global arch_alt
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch_alt = ops.getEnv("ARCH_ALT")

def MAIN_ENV(args):
    set_global(args)
    print ops.getEnv("ARCH_ALT")
    print ops.getEnv("DO_DEBOOTSTRAP")
    if arch_alt == "armel":
        ops.exportEnv(ops.setEnv("ARCH", "arm"))
    elif arch_alt == "x86_64":
        #ops.exportEnv(ops.setEnv("ARCH", "amd64"))
        ops.exportEnv(ops.setEnv("ARCH", "x86_64"))
    elif arch_alt == "any":
        ops.exportEnv(ops.setEnv("ARCH", "amd64"))
    else:
        sys.exit(1)

    ops.exportEnv(ops.setEnv("SDKSTAGE", output_dir + "/sdkstage"))
    ops.exportEnv(ops.setEnv("ARCH_ROOTFS", output_dir + "/rootfs"))
    ops.exportEnv(ops.setEnv("PACKAGES_DIR", output_dir + "/packages_dir"))
    ops.exportEnv(ops.setEnv("BASE_ROOTFS_DIR", output_dir))
    ops.exportEnv(ops.setEnv("OUTPUT_ROOTFS_DIR", output_dir))
    return False

def MAIN_EXTRACT(args):
    set_global(args)
    ops.mkdir(ops.getEnv("SDKSTAGE"))
    ops.mkdir(ops.getEnv("ARCH_ROOTFS"))
    ops.mkdir(ops.getEnv("PACKAGES_DIR"))
    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)
    return False

def MAIN_BUILD(args):
    set_global(args)
    return False

def MAIN_INSTALL(args):
    set_global(args)
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)

