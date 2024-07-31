---
layout: container
name:  "quay.io/biocontainers/danpos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/danpos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/danpos/container.yaml"
updated_at: "2024-07-31 02:49:05.000086"
latest: "2.2.2--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/danpos"
aliases:
 - "danpos.py"
 - "functions.py"
 - "lib.py"
 - "reads.py"
 - "summits.py"
 - "wig.py"
 - "wigs.py"
 - "wiq.py"
 - "f2py2"
 - "f2py2.7"
 - "bcftools"
 - "vcfutils.pl"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
versions:
 - "2.2.2--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for danpos"
config: {"url": "https://biocontainers.pro/tools/danpos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for danpos", "latest": {"2.2.2--hdfd78af_2": "sha256:b618af123e54b5df4f0b6f4ef61bcdb64e816c583fd28d6c61404081f24237e0"}, "tags": {"2.2.2--hdfd78af_2": "sha256:b618af123e54b5df4f0b6f4ef61bcdb64e816c583fd28d6c61404081f24237e0"}, "docker": "quay.io/biocontainers/danpos", "aliases": {"danpos.py": "/usr/local/bin/danpos.py", "functions.py": "/usr/local/bin/functions.py", "lib.py": "/usr/local/bin/lib.py", "reads.py": "/usr/local/bin/reads.py", "summits.py": "/usr/local/bin/summits.py", "wig.py": "/usr/local/bin/wig.py", "wigs.py": "/usr/local/bin/wigs.py", "wiq.py": "/usr/local/bin/wiq.py", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/danpos.
shpc-registry automated BioContainers addition for danpos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/danpos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/danpos:2.2.2--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/danpos/2.2.2--hdfd78af_2
$ module help quay.io/biocontainers/danpos/2.2.2--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### danpos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### danpos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### danpos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### danpos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### danpos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### danpos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### danpos.py

```bash
$ singularity exec <container> /usr/local/bin/danpos.py
$ podman run --it --rm --entrypoint /usr/local/bin/danpos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/danpos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### functions.py

```bash
$ singularity exec <container> /usr/local/bin/functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lib.py

```bash
$ singularity exec <container> /usr/local/bin/lib.py
$ podman run --it --rm --entrypoint /usr/local/bin/lib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reads.py

```bash
$ singularity exec <container> /usr/local/bin/reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summits.py

```bash
$ singularity exec <container> /usr/local/bin/summits.py
$ podman run --it --rm --entrypoint /usr/local/bin/summits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wig.py

```bash
$ singularity exec <container> /usr/local/bin/wig.py
$ podman run --it --rm --entrypoint /usr/local/bin/wig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wig.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigs.py

```bash
$ singularity exec <container> /usr/local/bin/wigs.py
$ podman run --it --rm --entrypoint /usr/local/bin/wigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wiq.py

```bash
$ singularity exec <container> /usr/local/bin/wiq.py
$ podman run --it --rm --entrypoint /usr/local/bin/wiq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wiq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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