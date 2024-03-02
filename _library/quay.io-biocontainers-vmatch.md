---
layout: container
name:  "quay.io/biocontainers/vmatch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vmatch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vmatch/container.yaml"
updated_at: "2024-03-02 02:28:04.545320"
latest: "2.3.0--hec16e2b_5"
container_url: "https://biocontainers.pro/tools/vmatch"
aliases:
 - "Vmatchtrans.pl"
 - "chain2dim"
 - "cleanpp.sh"
 - "matchcluster"
 - "mkdna6idx"
 - "mkvtree"
 - "repfind.pl"
 - "upgradeprj.pl"
 - "vendian"
 - "vmatch"
 - "vmatchselect"
 - "vmigrate.sh"
 - "vseqinfo"
 - "vseqselect"
 - "vstree2tex"
 - "vsubseqselect"
 - "conda_build.sh"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.3.0--hec16e2b_4"
 - "2.3.0--hec16e2b_5"
description: "shpc-registry automated BioContainers addition for vmatch"
config: {"url": "https://biocontainers.pro/tools/vmatch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vmatch", "latest": {"2.3.0--hec16e2b_5": "sha256:faf4d6f1b954f075f472fbffaac5b064faf07774b40cb59713bb69f2dffa9e4b"}, "tags": {"2.3.0--hec16e2b_4": "sha256:23c75961f1aa6960e280955628070b0f90984464fa25dda23d5a9e3d0b0425b5", "2.3.0--hec16e2b_5": "sha256:faf4d6f1b954f075f472fbffaac5b064faf07774b40cb59713bb69f2dffa9e4b"}, "docker": "quay.io/biocontainers/vmatch", "aliases": {"Vmatchtrans.pl": "/usr/local/bin/Vmatchtrans.pl", "chain2dim": "/usr/local/bin/chain2dim", "cleanpp.sh": "/usr/local/bin/cleanpp.sh", "matchcluster": "/usr/local/bin/matchcluster", "mkdna6idx": "/usr/local/bin/mkdna6idx", "mkvtree": "/usr/local/bin/mkvtree", "repfind.pl": "/usr/local/bin/repfind.pl", "upgradeprj.pl": "/usr/local/bin/upgradeprj.pl", "vendian": "/usr/local/bin/vendian", "vmatch": "/usr/local/bin/vmatch", "vmatchselect": "/usr/local/bin/vmatchselect", "vmigrate.sh": "/usr/local/bin/vmigrate.sh", "vseqinfo": "/usr/local/bin/vseqinfo", "vseqselect": "/usr/local/bin/vseqselect", "vstree2tex": "/usr/local/bin/vstree2tex", "vsubseqselect": "/usr/local/bin/vsubseqselect", "conda_build.sh": "/usr/local/bin/conda_build.sh", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vmatch.
shpc-registry automated BioContainers addition for vmatch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vmatch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vmatch:2.3.0--hec16e2b_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vmatch/2.3.0--hec16e2b_5
$ module help quay.io/biocontainers/vmatch/2.3.0--hec16e2b_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vmatch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vmatch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vmatch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vmatch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vmatch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vmatch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Vmatchtrans.pl

```bash
$ singularity exec <container> /usr/local/bin/Vmatchtrans.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Vmatchtrans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Vmatchtrans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chain2dim

```bash
$ singularity exec <container> /usr/local/bin/chain2dim
$ podman run --it --rm --entrypoint /usr/local/bin/chain2dim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chain2dim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanpp.sh

```bash
$ singularity exec <container> /usr/local/bin/cleanpp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cleanpp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanpp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matchcluster

```bash
$ singularity exec <container> /usr/local/bin/matchcluster
$ podman run --it --rm --entrypoint /usr/local/bin/matchcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matchcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkdna6idx

```bash
$ singularity exec <container> /usr/local/bin/mkdna6idx
$ podman run --it --rm --entrypoint /usr/local/bin/mkdna6idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkdna6idx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkvtree

```bash
$ singularity exec <container> /usr/local/bin/mkvtree
$ podman run --it --rm --entrypoint /usr/local/bin/mkvtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkvtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repfind.pl

```bash
$ singularity exec <container> /usr/local/bin/repfind.pl
$ podman run --it --rm --entrypoint /usr/local/bin/repfind.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repfind.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upgradeprj.pl

```bash
$ singularity exec <container> /usr/local/bin/upgradeprj.pl
$ podman run --it --rm --entrypoint /usr/local/bin/upgradeprj.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upgradeprj.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vendian

```bash
$ singularity exec <container> /usr/local/bin/vendian
$ podman run --it --rm --entrypoint /usr/local/bin/vendian   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vendian   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmatch

```bash
$ singularity exec <container> /usr/local/bin/vmatch
$ podman run --it --rm --entrypoint /usr/local/bin/vmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmatchselect

```bash
$ singularity exec <container> /usr/local/bin/vmatchselect
$ podman run --it --rm --entrypoint /usr/local/bin/vmatchselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmatchselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmigrate.sh

```bash
$ singularity exec <container> /usr/local/bin/vmigrate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/vmigrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmigrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vseqinfo

```bash
$ singularity exec <container> /usr/local/bin/vseqinfo
$ podman run --it --rm --entrypoint /usr/local/bin/vseqinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vseqinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vseqselect

```bash
$ singularity exec <container> /usr/local/bin/vseqselect
$ podman run --it --rm --entrypoint /usr/local/bin/vseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vstree2tex

```bash
$ singularity exec <container> /usr/local/bin/vstree2tex
$ podman run --it --rm --entrypoint /usr/local/bin/vstree2tex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vstree2tex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsubseqselect

```bash
$ singularity exec <container> /usr/local/bin/vsubseqselect
$ podman run --it --rm --entrypoint /usr/local/bin/vsubseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsubseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda_build.sh

```bash
$ singularity exec <container> /usr/local/bin/conda_build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda_build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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