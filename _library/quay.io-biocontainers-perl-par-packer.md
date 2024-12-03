---
layout: container
name:  "quay.io/biocontainers/perl-par-packer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-par-packer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-par-packer/container.yaml"
updated_at: "2024-12-03 03:16:42.427063"
latest: "1.036--pl5321h031d066_5"
container_url: "https://biocontainers.pro/tools/perl-par-packer"
aliases:
 - "crc32"
 - "par.pl"
 - "parl"
 - "parldyn"
 - "pp"
 - "scandeps.pl"
 - "tkpp"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.036--pl5321hec16e2b_4"
 - "1.036--pl5321h031d066_5"
description: "shpc-registry automated BioContainers addition for perl-par-packer"
config: {"url": "https://biocontainers.pro/tools/perl-par-packer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-par-packer", "latest": {"1.036--pl5321h031d066_5": "sha256:0d5e19bb4dfe688d0962f4e17f871477777e3f4c862ba64a080c0a9e93d7f478"}, "tags": {"1.036--pl5321hec16e2b_4": "sha256:648ab0f4fbb341d322422151868af62bedc37103071f89afdccffe68be4aa69d", "1.036--pl5321h031d066_5": "sha256:0d5e19bb4dfe688d0962f4e17f871477777e3f4c862ba64a080c0a9e93d7f478"}, "docker": "quay.io/biocontainers/perl-par-packer", "aliases": {"crc32": "/usr/local/bin/crc32", "par.pl": "/usr/local/bin/par.pl", "parl": "/usr/local/bin/parl", "parldyn": "/usr/local/bin/parldyn", "pp": "/usr/local/bin/pp", "scandeps.pl": "/usr/local/bin/scandeps.pl", "tkpp": "/usr/local/bin/tkpp", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-par-packer.
shpc-registry automated BioContainers addition for perl-par-packer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-par-packer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-par-packer:1.036--pl5321h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-par-packer/1.036--pl5321h031d066_5
$ module help quay.io/biocontainers/perl-par-packer/1.036--pl5321h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-par-packer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-par-packer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-par-packer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-par-packer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-par-packer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-par-packer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### par.pl

```bash
$ singularity exec <container> /usr/local/bin/par.pl
$ podman run --it --rm --entrypoint /usr/local/bin/par.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/par.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parl

```bash
$ singularity exec <container> /usr/local/bin/parl
$ podman run --it --rm --entrypoint /usr/local/bin/parl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parldyn

```bash
$ singularity exec <container> /usr/local/bin/parldyn
$ podman run --it --rm --entrypoint /usr/local/bin/parldyn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parldyn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pp

```bash
$ singularity exec <container> /usr/local/bin/pp
$ podman run --it --rm --entrypoint /usr/local/bin/pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scandeps.pl

```bash
$ singularity exec <container> /usr/local/bin/scandeps.pl
$ podman run --it --rm --entrypoint /usr/local/bin/scandeps.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scandeps.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tkpp

```bash
$ singularity exec <container> /usr/local/bin/tkpp
$ podman run --it --rm --entrypoint /usr/local/bin/tkpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tkpp   -v ${PWD} -w ${PWD} <container> -c " $@"
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