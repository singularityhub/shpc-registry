---
layout: container
name:  "quay.io/biocontainers/tdrmapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tdrmapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tdrmapper/container.yaml"
updated_at: "2024-05-10 03:06:17.111867"
latest: "1.1--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/tdrmapper"
aliases:
 - "TdrMappingScripts.pl"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "1.1--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for tdrmapper"
config: {"url": "https://biocontainers.pro/tools/tdrmapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tdrmapper", "latest": {"1.1--hdfd78af_5": "sha256:63d40fc465e3c2aa37677ddedc0ada4e9fbae29b1893ab652d55fc403f519733"}, "tags": {"1.1--hdfd78af_5": "sha256:63d40fc465e3c2aa37677ddedc0ada4e9fbae29b1893ab652d55fc403f519733"}, "docker": "quay.io/biocontainers/tdrmapper", "aliases": {"TdrMappingScripts.pl": "/usr/local/bin/TdrMappingScripts.pl", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tdrmapper.
shpc-registry automated BioContainers addition for tdrmapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tdrmapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tdrmapper:1.1--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tdrmapper/1.1--hdfd78af_5
$ module help quay.io/biocontainers/tdrmapper/1.1--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tdrmapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tdrmapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tdrmapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tdrmapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tdrmapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tdrmapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TdrMappingScripts.pl

```bash
$ singularity exec <container> /usr/local/bin/TdrMappingScripts.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TdrMappingScripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TdrMappingScripts.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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