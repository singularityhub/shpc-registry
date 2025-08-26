---
layout: container
name:  "quay.io/biocontainers/strling"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strling/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strling/container.yaml"
updated_at: "2025-08-26 03:59:32.505004"
latest: "0.5.2--hbbffb53_1"
container_url: "https://biocontainers.pro/tools/strling"
aliases:
 - "bg-bpipe"
 - "bpipe"
 - "bpipe-groovy"
 - "bpipe-pbspro.sh"
 - "bpipe-slurm.sh"
 - "bpipe-torque.sh"
 - "bpipe-utils.sh"
 - "groovy_script"
 - "strling"
 - "strling-outliers.py"
 - "jpackage"
 - "basenc"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
versions:
 - "0.5.1--h8a6b41c_3"
 - "0.5.1--h04c669c_4"
 - "0.5.2--h04c669c_0"
 - "0.5.2--hbbffb53_1"
description: "shpc-registry automated BioContainers addition for strling"
config: {"url": "https://biocontainers.pro/tools/strling", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strling", "latest": {"0.5.2--hbbffb53_1": "sha256:fb0d2381ecbe2356717048d102e18af7187cfe3a852e6c4d81e6ce9002d72b6f"}, "tags": {"0.5.1--h8a6b41c_3": "sha256:7165d1845c2e8b1f9c071e7369924958d3a6dbde32d8758bcbef5eb3c0073e33", "0.5.1--h04c669c_4": "sha256:48f282d9efac3a12f7957e1587214a295619bea0e44fe2eeba55dc6d6f7aa80b", "0.5.2--h04c669c_0": "sha256:7e1dde9deaaf9002d59706385eb6433dbf58792d25acaa3bc05d1b42b80adefe", "0.5.2--hbbffb53_1": "sha256:fb0d2381ecbe2356717048d102e18af7187cfe3a852e6c4d81e6ce9002d72b6f"}, "docker": "quay.io/biocontainers/strling", "aliases": {"bg-bpipe": "/usr/local/bin/bg-bpipe", "bpipe": "/usr/local/bin/bpipe", "bpipe-groovy": "/usr/local/bin/bpipe-groovy", "bpipe-pbspro.sh": "/usr/local/bin/bpipe-pbspro.sh", "bpipe-slurm.sh": "/usr/local/bin/bpipe-slurm.sh", "bpipe-torque.sh": "/usr/local/bin/bpipe-torque.sh", "bpipe-utils.sh": "/usr/local/bin/bpipe-utils.sh", "groovy_script": "/usr/local/bin/groovy_script", "strling": "/usr/local/bin/strling", "strling-outliers.py": "/usr/local/bin/strling-outliers.py", "jpackage": "/usr/local/bin/jpackage", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strling.
shpc-registry automated BioContainers addition for strling
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strling
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strling:0.5.2--hbbffb53_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strling/0.5.2--hbbffb53_1
$ module help quay.io/biocontainers/strling/0.5.2--hbbffb53_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strling-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strling-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strling-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strling-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strling-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strling-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bg-bpipe

```bash
$ singularity exec <container> /usr/local/bin/bg-bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe

```bash
$ singularity exec <container> /usr/local/bin/bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-groovy

```bash
$ singularity exec <container> /usr/local/bin/bpipe-groovy
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-groovy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-groovy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-pbspro.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-pbspro.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-slurm.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-slurm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-torque.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-torque.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-utils.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-utils.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groovy_script

```bash
$ singularity exec <container> /usr/local/bin/groovy_script
$ podman run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strling

```bash
$ singularity exec <container> /usr/local/bin/strling
$ podman run --it --rm --entrypoint /usr/local/bin/strling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strling-outliers.py

```bash
$ singularity exec <container> /usr/local/bin/strling-outliers.py
$ podman run --it --rm --entrypoint /usr/local/bin/strling-outliers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strling-outliers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
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