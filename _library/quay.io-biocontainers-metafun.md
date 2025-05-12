---
layout: container
name:  "quay.io/biocontainers/metafun"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metafun/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metafun/container.yaml"
updated_at: "2025-05-12 03:47:00.201941"
latest: "0.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metafun"
aliases:
 - "apptainer"
 - "cnitool"
 - "dash-update-components"
 - "fuse-overlayfs"
 - "hatchling"
 - "metafun"
 - "mksquashfs"
 - "mount.fuse3"
 - "run-singularity"
 - "scmp_sys_resolver"
 - "singularity"
 - "sqfscat"
 - "sqfstar"
 - "squashfuse"
 - "squashfuse_ll"
 - "sylph"
 - "unsquashfs"
 - "renderer"
 - "bsdunzip"
 - "dash-generate-components"
 - "nextflow.bak"
 - "nextflow"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "flask"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "basenc"
 - "b2sum"
 - "ls"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
 - "chown"
 - "chroot"
versions:
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for metafun"
config: {"url": "https://biocontainers.pro/tools/metafun", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metafun", "latest": {"0.3.0--pyhdfd78af_0": "sha256:6a6d0ae6fc7ef3be9c293e5614a693a00bb15fbd4d95aada38cae4bcfd8bef13"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:e5b8f5ddb50a9cf22a3343c5fbb4f64bb281056296b9b8fe6a4417d2ff513c8a", "0.3.0--pyhdfd78af_0": "sha256:6a6d0ae6fc7ef3be9c293e5614a693a00bb15fbd4d95aada38cae4bcfd8bef13"}, "docker": "quay.io/biocontainers/metafun", "aliases": {"apptainer": "/usr/local/bin/apptainer", "cnitool": "/usr/local/bin/cnitool", "dash-update-components": "/usr/local/bin/dash-update-components", "fuse-overlayfs": "/usr/local/bin/fuse-overlayfs", "hatchling": "/usr/local/bin/hatchling", "metafun": "/usr/local/bin/metafun", "mksquashfs": "/usr/local/bin/mksquashfs", "mount.fuse3": "/usr/local/bin/mount.fuse3", "run-singularity": "/usr/local/bin/run-singularity", "scmp_sys_resolver": "/usr/local/bin/scmp_sys_resolver", "singularity": "/usr/local/bin/singularity", "sqfscat": "/usr/local/bin/sqfscat", "sqfstar": "/usr/local/bin/sqfstar", "squashfuse": "/usr/local/bin/squashfuse", "squashfuse_ll": "/usr/local/bin/squashfuse_ll", "sylph": "/usr/local/bin/sylph", "unsquashfs": "/usr/local/bin/unsquashfs", "renderer": "/usr/local/bin/renderer", "bsdunzip": "/usr/local/bin/bsdunzip", "dash-generate-components": "/usr/local/bin/dash-generate-components", "nextflow.bak": "/usr/local/bin/nextflow.bak", "nextflow": "/usr/local/bin/nextflow", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "flask": "/usr/local/bin/flask", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metafun.
singularity registry hpc automated addition for metafun
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metafun
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metafun:0.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metafun/0.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/metafun/0.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metafun-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metafun-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metafun-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metafun-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metafun-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metafun-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### apptainer

```bash
$ singularity exec <container> /usr/local/bin/apptainer
$ podman run --it --rm --entrypoint /usr/local/bin/apptainer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/apptainer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnitool

```bash
$ singularity exec <container> /usr/local/bin/cnitool
$ podman run --it --rm --entrypoint /usr/local/bin/cnitool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnitool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-update-components

```bash
$ singularity exec <container> /usr/local/bin/dash-update-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-overlayfs

```bash
$ singularity exec <container> /usr/local/bin/fuse-overlayfs
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-overlayfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-overlayfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hatchling

```bash
$ singularity exec <container> /usr/local/bin/hatchling
$ podman run --it --rm --entrypoint /usr/local/bin/hatchling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hatchling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metafun

```bash
$ singularity exec <container> /usr/local/bin/metafun
$ podman run --it --rm --entrypoint /usr/local/bin/metafun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metafun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mksquashfs

```bash
$ singularity exec <container> /usr/local/bin/mksquashfs
$ podman run --it --rm --entrypoint /usr/local/bin/mksquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mksquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mount.fuse3

```bash
$ singularity exec <container> /usr/local/bin/mount.fuse3
$ podman run --it --rm --entrypoint /usr/local/bin/mount.fuse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mount.fuse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-singularity

```bash
$ singularity exec <container> /usr/local/bin/run-singularity
$ podman run --it --rm --entrypoint /usr/local/bin/run-singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scmp_sys_resolver

```bash
$ singularity exec <container> /usr/local/bin/scmp_sys_resolver
$ podman run --it --rm --entrypoint /usr/local/bin/scmp_sys_resolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scmp_sys_resolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singularity

```bash
$ singularity exec <container> /usr/local/bin/singularity
$ podman run --it --rm --entrypoint /usr/local/bin/singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singularity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqfscat

```bash
$ singularity exec <container> /usr/local/bin/sqfscat
$ podman run --it --rm --entrypoint /usr/local/bin/sqfscat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqfscat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqfstar

```bash
$ singularity exec <container> /usr/local/bin/sqfstar
$ podman run --it --rm --entrypoint /usr/local/bin/sqfstar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqfstar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### squashfuse

```bash
$ singularity exec <container> /usr/local/bin/squashfuse
$ podman run --it --rm --entrypoint /usr/local/bin/squashfuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/squashfuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### squashfuse_ll

```bash
$ singularity exec <container> /usr/local/bin/squashfuse_ll
$ podman run --it --rm --entrypoint /usr/local/bin/squashfuse_ll   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/squashfuse_ll   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sylph

```bash
$ singularity exec <container> /usr/local/bin/sylph
$ podman run --it --rm --entrypoint /usr/local/bin/sylph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sylph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unsquashfs

```bash
$ singularity exec <container> /usr/local/bin/unsquashfs
$ podman run --it --rm --entrypoint /usr/local/bin/unsquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unsquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow

```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ls

```bash
$ singularity exec <container> /usr/local/bin/ls
$ podman run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chcon

```bash
$ singularity exec <container> /usr/local/bin/chcon
$ podman run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chgrp

```bash
$ singularity exec <container> /usr/local/bin/chgrp
$ podman run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmod

```bash
$ singularity exec <container> /usr/local/bin/chmod
$ podman run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chown

```bash
$ singularity exec <container> /usr/local/bin/chown
$ podman run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chroot

```bash
$ singularity exec <container> /usr/local/bin/chroot
$ podman run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
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