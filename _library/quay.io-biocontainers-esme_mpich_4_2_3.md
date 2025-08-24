---
layout: container
name:  "quay.io/biocontainers/esme_mpich_4_2_3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_mpich_4_2_3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_mpich_4_2_3/container.yaml"
updated_at: "2025-08-24 03:38:49.599266"
latest: "1.0.0--mpich_ha3949f8_0"
container_url: "https://biocontainers.pro/tools/esme_mpich_4_2_3"
aliases:
 - "ESMF_PrintInfo"
 - "ESMF_PrintInfoC"
 - "ESMF_Regrid"
 - "ESMF_RegridWeightGen"
 - "ESMF_Scrip2Unstruct"
 - "ESMF_WebServController"
 - "ESMX_Builder"
 - "cdfdiff"
 - "chacl"
 - "getfacl"
 - "h5pcc"
 - "h5perf"
 - "h5pfc"
 - "nc4print"
 - "ncmpidiff"
 - "ncmpidump"
 - "ncmpigen"
 - "ncoffsets"
 - "ncvalidator"
 - "ocprint"
 - "ph5diff"
 - "pnetcdf-config"
 - "pnetcdf_version"
 - "setfacl"
 - "gost12-256-hash"
 - "gost12-512-hash"
 - "h5fuse"
 - "edonr256-hash"
 - "edonr512-hash"
 - "ccmake"
 - "cmake"
 - "cpack"
 - "ctest"
 - "ed2k-link"
 - "has160-hash"
 - "magnet-link"
 - "rhash"
 - "sfv-hash"
 - "tiger-hash"
 - "tth-hash"
 - "ucx_perftest_daemon"
 - "whirlpool-hash"
 - "nf-config"
 - "mpichversion"
 - "mpivars"
 - "parkill"
 - "hydra_nameserver"
 - "hydra_persist"
 - "hydra_pmi_proxy"
versions:
 - "1.0.0--mpich_ha3949f8_0"
description: "singularity registry hpc automated addition for esme_mpich_4_2_3"
config: {"url": "https://biocontainers.pro/tools/esme_mpich_4_2_3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_mpich_4_2_3", "latest": {"1.0.0--mpich_ha3949f8_0": "sha256:6e48db285688c73db966de23234dcec69b70e61227d9e0d0a3557f487c08360d"}, "tags": {"1.0.0--mpich_ha3949f8_0": "sha256:6e48db285688c73db966de23234dcec69b70e61227d9e0d0a3557f487c08360d"}, "docker": "quay.io/biocontainers/esme_mpich_4_2_3", "aliases": {"ESMF_PrintInfo": "/usr/local/bin/ESMF_PrintInfo", "ESMF_PrintInfoC": "/usr/local/bin/ESMF_PrintInfoC", "ESMF_Regrid": "/usr/local/bin/ESMF_Regrid", "ESMF_RegridWeightGen": "/usr/local/bin/ESMF_RegridWeightGen", "ESMF_Scrip2Unstruct": "/usr/local/bin/ESMF_Scrip2Unstruct", "ESMF_WebServController": "/usr/local/bin/ESMF_WebServController", "ESMX_Builder": "/usr/local/bin/ESMX_Builder", "cdfdiff": "/usr/local/bin/cdfdiff", "chacl": "/usr/local/bin/chacl", "getfacl": "/usr/local/bin/getfacl", "h5pcc": "/usr/local/bin/h5pcc", "h5perf": "/usr/local/bin/h5perf", "h5pfc": "/usr/local/bin/h5pfc", "nc4print": "/usr/local/bin/nc4print", "ncmpidiff": "/usr/local/bin/ncmpidiff", "ncmpidump": "/usr/local/bin/ncmpidump", "ncmpigen": "/usr/local/bin/ncmpigen", "ncoffsets": "/usr/local/bin/ncoffsets", "ncvalidator": "/usr/local/bin/ncvalidator", "ocprint": "/usr/local/bin/ocprint", "ph5diff": "/usr/local/bin/ph5diff", "pnetcdf-config": "/usr/local/bin/pnetcdf-config", "pnetcdf_version": "/usr/local/bin/pnetcdf_version", "setfacl": "/usr/local/bin/setfacl", "gost12-256-hash": "/usr/local/bin/gost12-256-hash", "gost12-512-hash": "/usr/local/bin/gost12-512-hash", "h5fuse": "/usr/local/bin/h5fuse", "edonr256-hash": "/usr/local/bin/edonr256-hash", "edonr512-hash": "/usr/local/bin/edonr512-hash", "ccmake": "/usr/local/bin/ccmake", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "ed2k-link": "/usr/local/bin/ed2k-link", "has160-hash": "/usr/local/bin/has160-hash", "magnet-link": "/usr/local/bin/magnet-link", "rhash": "/usr/local/bin/rhash", "sfv-hash": "/usr/local/bin/sfv-hash", "tiger-hash": "/usr/local/bin/tiger-hash", "tth-hash": "/usr/local/bin/tth-hash", "ucx_perftest_daemon": "/usr/local/bin/ucx_perftest_daemon", "whirlpool-hash": "/usr/local/bin/whirlpool-hash", "nf-config": "/usr/local/bin/nf-config", "mpichversion": "/usr/local/bin/mpichversion", "mpivars": "/usr/local/bin/mpivars", "parkill": "/usr/local/bin/parkill", "hydra_nameserver": "/usr/local/bin/hydra_nameserver", "hydra_persist": "/usr/local/bin/hydra_persist", "hydra_pmi_proxy": "/usr/local/bin/hydra_pmi_proxy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_mpich_4_2_3.
singularity registry hpc automated addition for esme_mpich_4_2_3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_mpich_4_2_3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_mpich_4_2_3:1.0.0--mpich_ha3949f8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_mpich_4_2_3/1.0.0--mpich_ha3949f8_0
$ module help quay.io/biocontainers/esme_mpich_4_2_3/1.0.0--mpich_ha3949f8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_mpich_4_2_3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_mpich_4_2_3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_mpich_4_2_3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_mpich_4_2_3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_mpich_4_2_3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_mpich_4_2_3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ESMF_PrintInfo

```bash
$ singularity exec <container> /usr/local/bin/ESMF_PrintInfo
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_PrintInfoC

```bash
$ singularity exec <container> /usr/local/bin/ESMF_PrintInfoC
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfoC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfoC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_Regrid

```bash
$ singularity exec <container> /usr/local/bin/ESMF_Regrid
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_Regrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_Regrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_RegridWeightGen

```bash
$ singularity exec <container> /usr/local/bin/ESMF_RegridWeightGen
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_RegridWeightGen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_RegridWeightGen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_Scrip2Unstruct

```bash
$ singularity exec <container> /usr/local/bin/ESMF_Scrip2Unstruct
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_Scrip2Unstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_Scrip2Unstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_WebServController

```bash
$ singularity exec <container> /usr/local/bin/ESMF_WebServController
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_WebServController   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_WebServController   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMX_Builder

```bash
$ singularity exec <container> /usr/local/bin/ESMX_Builder
$ podman run --it --rm --entrypoint /usr/local/bin/ESMX_Builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMX_Builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdfdiff

```bash
$ singularity exec <container> /usr/local/bin/cdfdiff
$ podman run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chacl

```bash
$ singularity exec <container> /usr/local/bin/chacl
$ podman run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfacl

```bash
$ singularity exec <container> /usr/local/bin/getfacl
$ podman run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pcc

```bash
$ singularity exec <container> /usr/local/bin/h5pcc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf

```bash
$ singularity exec <container> /usr/local/bin/h5perf
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pfc

```bash
$ singularity exec <container> /usr/local/bin/h5pfc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc4print

```bash
$ singularity exec <container> /usr/local/bin/nc4print
$ podman run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidiff

```bash
$ singularity exec <container> /usr/local/bin/ncmpidiff
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidump

```bash
$ singularity exec <container> /usr/local/bin/ncmpidump
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpigen

```bash
$ singularity exec <container> /usr/local/bin/ncmpigen
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncoffsets

```bash
$ singularity exec <container> /usr/local/bin/ncoffsets
$ podman run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncvalidator

```bash
$ singularity exec <container> /usr/local/bin/ncvalidator
$ podman run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocprint

```bash
$ singularity exec <container> /usr/local/bin/ocprint
$ podman run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ph5diff

```bash
$ singularity exec <container> /usr/local/bin/ph5diff
$ podman run --it --rm --entrypoint /usr/local/bin/ph5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ph5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf-config

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf-config
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf_version

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf_version
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfacl

```bash
$ singularity exec <container> /usr/local/bin/setfacl
$ podman run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-256-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-512-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr256-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr512-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccmake

```bash
$ singularity exec <container> /usr/local/bin/ccmake
$ podman run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmake

```bash
$ singularity exec <container> /usr/local/bin/cmake
$ podman run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpack

```bash
$ singularity exec <container> /usr/local/bin/cpack
$ podman run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctest

```bash
$ singularity exec <container> /usr/local/bin/ctest
$ podman run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ed2k-link

```bash
$ singularity exec <container> /usr/local/bin/ed2k-link
$ podman run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has160-hash

```bash
$ singularity exec <container> /usr/local/bin/has160-hash
$ podman run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magnet-link

```bash
$ singularity exec <container> /usr/local/bin/magnet-link
$ podman run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rhash

```bash
$ singularity exec <container> /usr/local/bin/rhash
$ podman run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfv-hash

```bash
$ singularity exec <container> /usr/local/bin/sfv-hash
$ podman run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfv-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiger-hash

```bash
$ singularity exec <container> /usr/local/bin/tiger-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiger-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tth-hash

```bash
$ singularity exec <container> /usr/local/bin/tth-hash
$ podman run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tth-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest_daemon

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whirlpool-hash

```bash
$ singularity exec <container> /usr/local/bin/whirlpool-hash
$ podman run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whirlpool-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-config

```bash
$ singularity exec <container> /usr/local/bin/nf-config
$ podman run --it --rm --entrypoint /usr/local/bin/nf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpichversion

```bash
$ singularity exec <container> /usr/local/bin/mpichversion
$ podman run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpivars

```bash
$ singularity exec <container> /usr/local/bin/mpivars
$ podman run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parkill

```bash
$ singularity exec <container> /usr/local/bin/parkill
$ podman run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_nameserver

```bash
$ singularity exec <container> /usr/local/bin/hydra_nameserver
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_persist

```bash
$ singularity exec <container> /usr/local/bin/hydra_persist
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_pmi_proxy

```bash
$ singularity exec <container> /usr/local/bin/hydra_pmi_proxy
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)