---
layout: container
name:  "quay.io/biocontainers/zorro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zorro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/zorro/container.yaml"
updated_at: "2025-11-16 03:48:02.022029"
latest: "2011.12.01--h7b50bb2_5"
container_url: "https://biocontainers.pro/tools/zorro"
aliases:
 - "zorro"
 - "zorro_dist.pl"
 - "FastTreeMP"
 - "FastTree"
 - "fasttree"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2011.12.01--hec16e2b_3"
 - "2011.12.01--h031d066_4"
 - "2011.12.01--h7b50bb2_5"
description: "shpc-registry automated BioContainers addition for zorro"
config: {"url": "https://biocontainers.pro/tools/zorro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zorro", "latest": {"2011.12.01--h7b50bb2_5": "sha256:285f24d2adb9462fa773c311fe51fec94b191653ffdad5fc3e34e88e7a7c18fc"}, "tags": {"2011.12.01--hec16e2b_3": "sha256:469cae7eb92606ec46a9b6996ac739c3ee4dca6622450080bf0c3ce7e42a3727", "2011.12.01--h031d066_4": "sha256:0c45c07bfbea29215a90901de1dd88760408d4ca80e31a8927b93bcab3dfa12e", "2011.12.01--h7b50bb2_5": "sha256:285f24d2adb9462fa773c311fe51fec94b191653ffdad5fc3e34e88e7a7c18fc"}, "docker": "quay.io/biocontainers/zorro", "aliases": {"zorro": "/usr/local/bin/zorro", "zorro_dist.pl": "/usr/local/bin/zorro_dist.pl", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zorro.
shpc-registry automated BioContainers addition for zorro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zorro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zorro:2011.12.01--h7b50bb2_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zorro/2011.12.01--h7b50bb2_5
$ module help quay.io/biocontainers/zorro/2011.12.01--h7b50bb2_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zorro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zorro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zorro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zorro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zorro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zorro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### zorro

```bash
$ singularity exec <container> /usr/local/bin/zorro
$ podman run --it --rm --entrypoint /usr/local/bin/zorro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zorro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zorro_dist.pl

```bash
$ singularity exec <container> /usr/local/bin/zorro_dist.pl
$ podman run --it --rm --entrypoint /usr/local/bin/zorro_dist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zorro_dist.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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