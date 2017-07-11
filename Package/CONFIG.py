import ops
import iopc

pkg_path = ""
output_dir = ""

def set_global(args):
    global pkg_path 
    global output_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]

def MAIN_ENV(args):
    set_global(args)
    print ops.getEnv("ARCH_ALT")
    print ops.getEnv("DO_DEBOOTSTRAP")

    ops.exportEnv(ops.setEnv("ARCH", "arm"))
    #ops.exportEnv(ops.setEnv("ARCH_ALT", "armhf"))
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

