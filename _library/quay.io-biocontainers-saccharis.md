---
layout: container
name:  "quay.io/biocontainers/saccharis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/saccharis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/saccharis/container.yaml"
updated_at: "2024-04-30 02:49:29.974091"
latest: "2.0.0.dev21--pyh7cba7a3_2"
container_url: "https://biocontainers.pro/tools/saccharis"
aliases:
 - "dotenv"
 - "hb-info"
 - "hmmscan_parser.py"
 - "modeltest-ng"
 - "modeltest-ng-mpi"
 - "run_dbcan"
 - "saccharis"
 - "saccharis-gui"
 - "saccharis.add_family_category"
 - "saccharis.make_family_files"
 - "saccharis.prune_seqs"
 - "saccharis.rename_user_file"
 - "saccharis.screen_cazome"
 - "saccharis.show_family_categories"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "dumpsexp"
 - "gpg-error"
 - "gpgrt-config"
 - "hmac256"
 - "libgcrypt-config"
 - "mpicalc"
 - "yat2m"
 - "lame"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
 - "attr"
 - "balsam"
 - "getfattr"
 - "lprodump"
 - "lrelease-pro"
 - "lupdate-pro"
 - "meshdebug"
versions:
 - "2.0.0.dev18--pyh7cba7a3_0"
 - "2.0.0.dev19--pyh7cba7a3_7"
 - "2.0.0.dev21--pyh7cba7a3_2"
description: "singularity registry hpc automated addition for saccharis"
config: {"url": "https://biocontainers.pro/tools/saccharis", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for saccharis", "latest": {"2.0.0.dev21--pyh7cba7a3_2": "sha256:9148c20f6e9fa6b949535b3cffec8c454cfa2ec59de38f3393d543b8b8fa1913"}, "tags": {"2.0.0.dev18--pyh7cba7a3_0": "sha256:b92c8dd0fd53dad9f8df94dfddb77931c844300e321e22fac9afc40383f3d17b", "2.0.0.dev19--pyh7cba7a3_7": "sha256:80261b1b938c39d7c1e13055ffde50e2eed8b974d16d84308e6afedb9db8b8a2", "2.0.0.dev21--pyh7cba7a3_2": "sha256:9148c20f6e9fa6b949535b3cffec8c454cfa2ec59de38f3393d543b8b8fa1913"}, "docker": "quay.io/biocontainers/saccharis", "aliases": {"dotenv": "/usr/local/bin/dotenv", "hb-info": "/usr/local/bin/hb-info", "hmmscan_parser.py": "/usr/local/bin/hmmscan_parser.py", "modeltest-ng": "/usr/local/bin/modeltest-ng", "modeltest-ng-mpi": "/usr/local/bin/modeltest-ng-mpi", "run_dbcan": "/usr/local/bin/run_dbcan", "saccharis": "/usr/local/bin/saccharis", "saccharis-gui": "/usr/local/bin/saccharis-gui", "saccharis.add_family_category": "/usr/local/bin/saccharis.add_family_category", "saccharis.make_family_files": "/usr/local/bin/saccharis.make_family_files", "saccharis.prune_seqs": "/usr/local/bin/saccharis.prune_seqs", "saccharis.rename_user_file": "/usr/local/bin/saccharis.rename_user_file", "saccharis.screen_cazome": "/usr/local/bin/saccharis.screen_cazome", "saccharis.show_family_categories": "/usr/local/bin/saccharis.show_family_categories", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "dumpsexp": "/usr/local/bin/dumpsexp", "gpg-error": "/usr/local/bin/gpg-error", "gpgrt-config": "/usr/local/bin/gpgrt-config", "hmac256": "/usr/local/bin/hmac256", "libgcrypt-config": "/usr/local/bin/libgcrypt-config", "mpicalc": "/usr/local/bin/mpicalc", "yat2m": "/usr/local/bin/yat2m", "lame": "/usr/local/bin/lame", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel", "attr": "/usr/local/bin/attr", "balsam": "/usr/local/bin/balsam", "getfattr": "/usr/local/bin/getfattr", "lprodump": "/usr/local/bin/lprodump", "lrelease-pro": "/usr/local/bin/lrelease-pro", "lupdate-pro": "/usr/local/bin/lupdate-pro", "meshdebug": "/usr/local/bin/meshdebug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/saccharis.
singularity registry hpc automated addition for saccharis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/saccharis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/saccharis:2.0.0.dev21--pyh7cba7a3_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/saccharis/2.0.0.dev21--pyh7cba7a3_2
$ module help quay.io/biocontainers/saccharis/2.0.0.dev21--pyh7cba7a3_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### saccharis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### saccharis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### saccharis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### saccharis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### saccharis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### saccharis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmscan_parser.py

```bash
$ singularity exec <container> /usr/local/bin/hmmscan_parser.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmmscan_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmscan_parser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### modeltest-ng

```bash
$ singularity exec <container> /usr/local/bin/modeltest-ng
$ podman run --it --rm --entrypoint /usr/local/bin/modeltest-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modeltest-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### modeltest-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/modeltest-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/modeltest-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modeltest-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_dbcan

```bash
$ singularity exec <container> /usr/local/bin/run_dbcan
$ podman run --it --rm --entrypoint /usr/local/bin/run_dbcan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_dbcan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis

```bash
$ singularity exec <container> /usr/local/bin/saccharis
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis-gui

```bash
$ singularity exec <container> /usr/local/bin/saccharis-gui
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis.add_family_category

```bash
$ singularity exec <container> /usr/local/bin/saccharis.add_family_category
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis.add_family_category   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis.add_family_category   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis.make_family_files

```bash
$ singularity exec <container> /usr/local/bin/saccharis.make_family_files
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis.make_family_files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis.make_family_files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis.prune_seqs

```bash
$ singularity exec <container> /usr/local/bin/saccharis.prune_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis.prune_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis.prune_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis.rename_user_file

```bash
$ singularity exec <container> /usr/local/bin/saccharis.rename_user_file
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis.rename_user_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis.rename_user_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis.screen_cazome

```bash
$ singularity exec <container> /usr/local/bin/saccharis.screen_cazome
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis.screen_cazome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis.screen_cazome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saccharis.show_family_categories

```bash
$ singularity exec <container> /usr/local/bin/saccharis.show_family_categories
$ podman run --it --rm --entrypoint /usr/local/bin/saccharis.show_family_categories   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saccharis.show_family_categories   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123

```bash
$ singularity exec <container> /usr/local/bin/mpg123
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-id3dump

```bash
$ singularity exec <container> /usr/local/bin/mpg123-id3dump
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-strip

```bash
$ singularity exec <container> /usr/local/bin/mpg123-strip
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### out123

```bash
$ singularity exec <container> /usr/local/bin/out123
$ podman run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsexp

```bash
$ singularity exec <container> /usr/local/bin/dumpsexp
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-error

```bash
$ singularity exec <container> /usr/local/bin/gpg-error
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgrt-config

```bash
$ singularity exec <container> /usr/local/bin/gpgrt-config
$ podman run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmac256

```bash
$ singularity exec <container> /usr/local/bin/hmac256
$ podman run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libgcrypt-config

```bash
$ singularity exec <container> /usr/local/bin/libgcrypt-config
$ podman run --it --rm --entrypoint /usr/local/bin/libgcrypt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libgcrypt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicalc

```bash
$ singularity exec <container> /usr/local/bin/mpicalc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yat2m

```bash
$ singularity exec <container> /usr/local/bin/yat2m
$ podman run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-build

```bash
$ singularity exec <container> /usr/local/bin/sip-build
$ podman run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-distinfo

```bash
$ singularity exec <container> /usr/local/bin/sip-distinfo
$ podman run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-install

```bash
$ singularity exec <container> /usr/local/bin/sip-install
$ podman run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-module

```bash
$ singularity exec <container> /usr/local/bin/sip-module
$ podman run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-sdist

```bash
$ singularity exec <container> /usr/local/bin/sip-sdist
$ podman run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-wheel

```bash
$ singularity exec <container> /usr/local/bin/sip-wheel
$ podman run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### attr

```bash
$ singularity exec <container> /usr/local/bin/attr
$ podman run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### balsam

```bash
$ singularity exec <container> /usr/local/bin/balsam
$ podman run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfattr

```bash
$ singularity exec <container> /usr/local/bin/getfattr
$ podman run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lprodump

```bash
$ singularity exec <container> /usr/local/bin/lprodump
$ podman run --it --rm --entrypoint /usr/local/bin/lprodump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lprodump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease-pro

```bash
$ singularity exec <container> /usr/local/bin/lrelease-pro
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate-pro

```bash
$ singularity exec <container> /usr/local/bin/lupdate-pro
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meshdebug

```bash
$ singularity exec <container> /usr/local/bin/meshdebug
$ podman run --it --rm --entrypoint /usr/local/bin/meshdebug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meshdebug   -v ${PWD} -w ${PWD} <container> -c " $@"
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