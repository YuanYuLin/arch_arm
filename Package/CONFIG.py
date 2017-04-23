import ops

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]

    ops.exportEnv(ops.setEnv("ARCH", "arm"))
    ops.exportEnv(ops.setEnv("ARCH_ALT", "armhf"))
    ops.exportEnv(ops.setEnv("SDKSTAGE", output_dir + "/sdkstage"))
    ops.exportEnv(ops.setEnv("ARCH_ROOTFS", output_dir + "/rootfs"))
    ops.exportEnv(ops.setEnv("PACKAGES_DIR", output_dir + "/packages_dir"))
    ops.exportEnv(ops.setEnv("BASE_ROOTFS_DIR", output_dir))
    return False

def MAIN_EXTRACT(args):
    output_dir = args["output_path"]
    ops.mkdir(ops.getEnv("SDKSTAGE"))
    ops.mkdir(ops.getEnv("ARCH_ROOTFS"))
    ops.mkdir(ops.getEnv("PACKAGES_DIR"))
    return False

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]
    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    output_dir = args["output_path"]

