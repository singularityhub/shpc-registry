---
layout: container
name:  "quay.io/biocontainers/cellrank-krylov"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cellrank-krylov/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cellrank-krylov/container.yaml"
updated_at: "2024-03-30 02:21:43.745667"
latest: "1.5.1--pyh1e54042_0"
container_url: "https://biocontainers.pro/tools/cellrank-krylov"
aliases:
 - "acpl"
 - "amk_ccc"
 - "amk_fft2"
 - "amk_grf"
 - "amk_hy"
 - "amk_m2"
 - "amk_p2"
 - "atst"
 - "dggath"
 - "dgmap"
 - "dgord"
 - "dgpart"
 - "dgscat"
 - "dgtst"
 - "dunamai"
 - "gbase"
 - "gcv"
 - "gmk_hy"
 - "gmk_m2"
 - "gmk_m3"
 - "gmk_msh"
 - "gmk_ub2"
 - "gmtst"
 - "gord"
 - "gotst"
 - "gout"
 - "gpart"
 - "gscat"
 - "gtst"
 - "loompy"
 - "mcv"
 - "mmk_m2"
 - "mmk_m3"
 - "mord"
 - "mtest"
 - "mtst"
 - "parmetis"
 - "pddrive"
 - "pddrive_spawn"
 - "pometis"
 - "ptest"
 - "scotch_esmumps"
 - "gmap"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "scanpy"
 - "oshCC"
versions:
 - "1.5.1--pyh1e54042_0"
description: "shpc-registry automated BioContainers addition for cellrank-krylov"
config: {"url": "https://biocontainers.pro/tools/cellrank-krylov", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cellrank-krylov", "latest": {"1.5.1--pyh1e54042_0": "sha256:e66608bf24b4fda39abc9327a2e2d087566c95bfbb9906fd8e2d64cf01666110"}, "tags": {"1.5.1--pyh1e54042_0": "sha256:e66608bf24b4fda39abc9327a2e2d087566c95bfbb9906fd8e2d64cf01666110"}, "docker": "quay.io/biocontainers/cellrank-krylov", "aliases": {"acpl": "/usr/local/bin/acpl", "amk_ccc": "/usr/local/bin/amk_ccc", "amk_fft2": "/usr/local/bin/amk_fft2", "amk_grf": "/usr/local/bin/amk_grf", "amk_hy": "/usr/local/bin/amk_hy", "amk_m2": "/usr/local/bin/amk_m2", "amk_p2": "/usr/local/bin/amk_p2", "atst": "/usr/local/bin/atst", "dggath": "/usr/local/bin/dggath", "dgmap": "/usr/local/bin/dgmap", "dgord": "/usr/local/bin/dgord", "dgpart": "/usr/local/bin/dgpart", "dgscat": "/usr/local/bin/dgscat", "dgtst": "/usr/local/bin/dgtst", "dunamai": "/usr/local/bin/dunamai", "gbase": "/usr/local/bin/gbase", "gcv": "/usr/local/bin/gcv", "gmk_hy": "/usr/local/bin/gmk_hy", "gmk_m2": "/usr/local/bin/gmk_m2", "gmk_m3": "/usr/local/bin/gmk_m3", "gmk_msh": "/usr/local/bin/gmk_msh", "gmk_ub2": "/usr/local/bin/gmk_ub2", "gmtst": "/usr/local/bin/gmtst", "gord": "/usr/local/bin/gord", "gotst": "/usr/local/bin/gotst", "gout": "/usr/local/bin/gout", "gpart": "/usr/local/bin/gpart", "gscat": "/usr/local/bin/gscat", "gtst": "/usr/local/bin/gtst", "loompy": "/usr/local/bin/loompy", "mcv": "/usr/local/bin/mcv", "mmk_m2": "/usr/local/bin/mmk_m2", "mmk_m3": "/usr/local/bin/mmk_m3", "mord": "/usr/local/bin/mord", "mtest": "/usr/local/bin/mtest", "mtst": "/usr/local/bin/mtst", "parmetis": "/usr/local/bin/parmetis", "pddrive": "/usr/local/bin/pddrive", "pddrive_spawn": "/usr/local/bin/pddrive_spawn", "pometis": "/usr/local/bin/pometis", "ptest": "/usr/local/bin/ptest", "scotch_esmumps": "/usr/local/bin/scotch_esmumps", "gmap": "/usr/local/bin/gmap", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "scanpy": "/usr/local/bin/scanpy", "oshCC": "/usr/local/bin/oshCC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cellrank-krylov.
shpc-registry automated BioContainers addition for cellrank-krylov
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cellrank-krylov
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cellrank-krylov:1.5.1--pyh1e54042_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cellrank-krylov/1.5.1--pyh1e54042_0
$ module help quay.io/biocontainers/cellrank-krylov/1.5.1--pyh1e54042_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cellrank-krylov-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cellrank-krylov-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cellrank-krylov-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cellrank-krylov-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cellrank-krylov-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cellrank-krylov-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### acpl

```bash
$ singularity exec <container> /usr/local/bin/acpl
$ podman run --it --rm --entrypoint /usr/local/bin/acpl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acpl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amk_ccc

```bash
$ singularity exec <container> /usr/local/bin/amk_ccc
$ podman run --it --rm --entrypoint /usr/local/bin/amk_ccc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amk_ccc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amk_fft2

```bash
$ singularity exec <container> /usr/local/bin/amk_fft2
$ podman run --it --rm --entrypoint /usr/local/bin/amk_fft2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amk_fft2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amk_grf

```bash
$ singularity exec <container> /usr/local/bin/amk_grf
$ podman run --it --rm --entrypoint /usr/local/bin/amk_grf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amk_grf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amk_hy

```bash
$ singularity exec <container> /usr/local/bin/amk_hy
$ podman run --it --rm --entrypoint /usr/local/bin/amk_hy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amk_hy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amk_m2

```bash
$ singularity exec <container> /usr/local/bin/amk_m2
$ podman run --it --rm --entrypoint /usr/local/bin/amk_m2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amk_m2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amk_p2

```bash
$ singularity exec <container> /usr/local/bin/amk_p2
$ podman run --it --rm --entrypoint /usr/local/bin/amk_p2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amk_p2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### atst

```bash
$ singularity exec <container> /usr/local/bin/atst
$ podman run --it --rm --entrypoint /usr/local/bin/atst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dggath

```bash
$ singularity exec <container> /usr/local/bin/dggath
$ podman run --it --rm --entrypoint /usr/local/bin/dggath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dggath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dgmap

```bash
$ singularity exec <container> /usr/local/bin/dgmap
$ podman run --it --rm --entrypoint /usr/local/bin/dgmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dgord

```bash
$ singularity exec <container> /usr/local/bin/dgord
$ podman run --it --rm --entrypoint /usr/local/bin/dgord   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgord   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dgpart

```bash
$ singularity exec <container> /usr/local/bin/dgpart
$ podman run --it --rm --entrypoint /usr/local/bin/dgpart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgpart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dgscat

```bash
$ singularity exec <container> /usr/local/bin/dgscat
$ podman run --it --rm --entrypoint /usr/local/bin/dgscat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgscat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dgtst

```bash
$ singularity exec <container> /usr/local/bin/dgtst
$ podman run --it --rm --entrypoint /usr/local/bin/dgtst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgtst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbase

```bash
$ singularity exec <container> /usr/local/bin/gbase
$ podman run --it --rm --entrypoint /usr/local/bin/gbase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbase   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcv

```bash
$ singularity exec <container> /usr/local/bin/gcv
$ podman run --it --rm --entrypoint /usr/local/bin/gcv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmk_hy

```bash
$ singularity exec <container> /usr/local/bin/gmk_hy
$ podman run --it --rm --entrypoint /usr/local/bin/gmk_hy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmk_hy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmk_m2

```bash
$ singularity exec <container> /usr/local/bin/gmk_m2
$ podman run --it --rm --entrypoint /usr/local/bin/gmk_m2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmk_m2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmk_m3

```bash
$ singularity exec <container> /usr/local/bin/gmk_m3
$ podman run --it --rm --entrypoint /usr/local/bin/gmk_m3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmk_m3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmk_msh

```bash
$ singularity exec <container> /usr/local/bin/gmk_msh
$ podman run --it --rm --entrypoint /usr/local/bin/gmk_msh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmk_msh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmk_ub2

```bash
$ singularity exec <container> /usr/local/bin/gmk_ub2
$ podman run --it --rm --entrypoint /usr/local/bin/gmk_ub2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmk_ub2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmtst

```bash
$ singularity exec <container> /usr/local/bin/gmtst
$ podman run --it --rm --entrypoint /usr/local/bin/gmtst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmtst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gord

```bash
$ singularity exec <container> /usr/local/bin/gord
$ podman run --it --rm --entrypoint /usr/local/bin/gord   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gord   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gotst

```bash
$ singularity exec <container> /usr/local/bin/gotst
$ podman run --it --rm --entrypoint /usr/local/bin/gotst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gotst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gout

```bash
$ singularity exec <container> /usr/local/bin/gout
$ podman run --it --rm --entrypoint /usr/local/bin/gout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpart

```bash
$ singularity exec <container> /usr/local/bin/gpart
$ podman run --it --rm --entrypoint /usr/local/bin/gpart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gscat

```bash
$ singularity exec <container> /usr/local/bin/gscat
$ podman run --it --rm --entrypoint /usr/local/bin/gscat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gscat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtst

```bash
$ singularity exec <container> /usr/local/bin/gtst
$ podman run --it --rm --entrypoint /usr/local/bin/gtst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcv

```bash
$ singularity exec <container> /usr/local/bin/mcv
$ podman run --it --rm --entrypoint /usr/local/bin/mcv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmk_m2

```bash
$ singularity exec <container> /usr/local/bin/mmk_m2
$ podman run --it --rm --entrypoint /usr/local/bin/mmk_m2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmk_m2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmk_m3

```bash
$ singularity exec <container> /usr/local/bin/mmk_m3
$ podman run --it --rm --entrypoint /usr/local/bin/mmk_m3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmk_m3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mord

```bash
$ singularity exec <container> /usr/local/bin/mord
$ podman run --it --rm --entrypoint /usr/local/bin/mord   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mord   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtest

```bash
$ singularity exec <container> /usr/local/bin/mtest
$ podman run --it --rm --entrypoint /usr/local/bin/mtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtst

```bash
$ singularity exec <container> /usr/local/bin/mtst
$ podman run --it --rm --entrypoint /usr/local/bin/mtst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parmetis

```bash
$ singularity exec <container> /usr/local/bin/parmetis
$ podman run --it --rm --entrypoint /usr/local/bin/parmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pddrive

```bash
$ singularity exec <container> /usr/local/bin/pddrive
$ podman run --it --rm --entrypoint /usr/local/bin/pddrive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pddrive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pddrive_spawn

```bash
$ singularity exec <container> /usr/local/bin/pddrive_spawn
$ podman run --it --rm --entrypoint /usr/local/bin/pddrive_spawn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pddrive_spawn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pometis

```bash
$ singularity exec <container> /usr/local/bin/pometis
$ podman run --it --rm --entrypoint /usr/local/bin/pometis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pometis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptest

```bash
$ singularity exec <container> /usr/local/bin/ptest
$ podman run --it --rm --entrypoint /usr/local/bin/ptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scotch_esmumps

```bash
$ singularity exec <container> /usr/local/bin/scotch_esmumps
$ podman run --it --rm --entrypoint /usr/local/bin/scotch_esmumps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scotch_esmumps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap

```bash
$ singularity exec <container> /usr/local/bin/gmap
$ podman run --it --rm --entrypoint /usr/local/bin/gmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /usr/local/bin/git-cvsserver
$ podman run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/git-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /usr/local/bin/git-shell
$ podman run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /usr/local/bin/git-upload-archive
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/git-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gitk

```bash
$ singularity exec <container> /usr/local/bin/gitk
$ podman run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
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