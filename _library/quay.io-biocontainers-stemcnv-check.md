---
layout: container
name:  "quay.io/biocontainers/stemcnv-check"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stemcnv-check/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stemcnv-check/container.yaml"
updated_at: "2025-11-02 03:56:11.594234"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/stemcnv-check"
aliases:
 - "apptainer"
 - "cnitool"
 - "deep"
 - "fuse-overlayfs"
 - "mksquashfs"
 - "mount.fuse3"
 - "run-singularity"
 - "scmp_sys_resolver"
 - "singularity"
 - "sqfscat"
 - "sqfstar"
 - "squashfuse"
 - "squashfuse_ll"
 - "stemcnv-check"
 - "unsquashfs"
 - "bsdunzip"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
 - "rst2xml"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "vba_extract.py"
 - "yte"
 - "plac_runner.py"
 - "docutils"
 - "pulptest"
 - "snakemake"
 - "cbc"
 - "clp"
 - "humanfriendly"
 - "tabulate"
 - "jupyter-trust"
versions:
 - "0.5.1--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_1"
 - "0.5.2--pyhdfd78af_0"
 - "0.5.4--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for stemcnv-check"
config: {"url": "https://biocontainers.pro/tools/stemcnv-check", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for stemcnv-check", "latest": {"1.0.0--pyhdfd78af_0": "sha256:3e7fcb0db98b9174ff52515029ec0d56420093c12fd2edeecf149b1ab2918f71"}, "tags": {"0.5.1--pyhdfd78af_0": "sha256:3c4994a79d5a149aec5e4870a6876992aac6cd00d426d47fabdd053f355feb37", "0.5.1--pyhdfd78af_1": "sha256:cf9d7c5d8824b146f8227ff78818b862cc11c7f3fa78f898809e85a950275a14", "0.5.2--pyhdfd78af_0": "sha256:8383d8026a43e79bc412553f05e7fde1950a4aa8f9b2756ef9418afe9e610a79", "0.5.4--pyhdfd78af_0": "sha256:fe545cbbafec489798ad833e156588bfcfe597f6717bcf7b00b3654e3c508b6a", "1.0.0--pyhdfd78af_0": "sha256:3e7fcb0db98b9174ff52515029ec0d56420093c12fd2edeecf149b1ab2918f71"}, "docker": "quay.io/biocontainers/stemcnv-check", "aliases": {"apptainer": "/usr/local/bin/apptainer", "cnitool": "/usr/local/bin/cnitool", "deep": "/usr/local/bin/deep", "fuse-overlayfs": "/usr/local/bin/fuse-overlayfs", "mksquashfs": "/usr/local/bin/mksquashfs", "mount.fuse3": "/usr/local/bin/mount.fuse3", "run-singularity": "/usr/local/bin/run-singularity", "scmp_sys_resolver": "/usr/local/bin/scmp_sys_resolver", "singularity": "/usr/local/bin/singularity", "sqfscat": "/usr/local/bin/sqfscat", "sqfstar": "/usr/local/bin/sqfstar", "squashfuse": "/usr/local/bin/squashfuse", "squashfuse_ll": "/usr/local/bin/squashfuse_ll", "stemcnv-check": "/usr/local/bin/stemcnv-check", "unsquashfs": "/usr/local/bin/unsquashfs", "bsdunzip": "/usr/local/bin/bsdunzip", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex", "rst2xml": "/usr/local/bin/rst2xml", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "vba_extract.py": "/usr/local/bin/vba_extract.py", "yte": "/usr/local/bin/yte", "plac_runner.py": "/usr/local/bin/plac_runner.py", "docutils": "/usr/local/bin/docutils", "pulptest": "/usr/local/bin/pulptest", "snakemake": "/usr/local/bin/snakemake", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "humanfriendly": "/usr/local/bin/humanfriendly", "tabulate": "/usr/local/bin/tabulate", "jupyter-trust": "/usr/local/bin/jupyter-trust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stemcnv-check.
singularity registry hpc automated addition for stemcnv-check
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stemcnv-check
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stemcnv-check:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stemcnv-check/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/stemcnv-check/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stemcnv-check-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stemcnv-check-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stemcnv-check-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stemcnv-check-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stemcnv-check-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stemcnv-check-inspect-deffile:

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


#### deep

```bash
$ singularity exec <container> /usr/local/bin/deep
$ podman run --it --rm --entrypoint /usr/local/bin/deep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-overlayfs

```bash
$ singularity exec <container> /usr/local/bin/fuse-overlayfs
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-overlayfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-overlayfs   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### stemcnv-check

```bash
$ singularity exec <container> /usr/local/bin/stemcnv-check
$ podman run --it --rm --entrypoint /usr/local/bin/stemcnv-check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stemcnv-check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unsquashfs

```bash
$ singularity exec <container> /usr/local/bin/unsquashfs
$ podman run --it --rm --entrypoint /usr/local/bin/unsquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unsquashfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml

```bash
$ singularity exec <container> /usr/local/bin/rst2xml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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