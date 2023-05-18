---
layout: container
name:  "quay.io/biocontainers/links"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/links/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/links/container.yaml"
updated_at: "2023-05-18 04:37:43.344110"
latest: "2.0.1--h9f5acd7_2"
container_url: "https://biocontainers.pro/tools/links"
aliases:
 - "LINKS"
 - "LINKS-make"
 - "LINKS-make-real"
 - "LINKS.pl"
 - "LINKS_CPP"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.0.1--h9f5acd7_2"
description: "shpc-registry automated BioContainers addition for links"
config: {"url": "https://biocontainers.pro/tools/links", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for links", "latest": {"2.0.1--h9f5acd7_2": "sha256:c8f95e2f3235a4b8bbaf8faa9c4533a9f7eb0f19c444cea01aabb75a10ec1c8f"}, "tags": {"2.0.1--h9f5acd7_2": "sha256:c8f95e2f3235a4b8bbaf8faa9c4533a9f7eb0f19c444cea01aabb75a10ec1c8f"}, "docker": "quay.io/biocontainers/links", "aliases": {"LINKS": "/usr/local/bin/LINKS", "LINKS-make": "/usr/local/bin/LINKS-make", "LINKS-make-real": "/usr/local/bin/LINKS-make-real", "LINKS.pl": "/usr/local/bin/LINKS.pl", "LINKS_CPP": "/usr/local/bin/LINKS_CPP", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/links.
shpc-registry automated BioContainers addition for links
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/links
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/links:2.0.1--h9f5acd7_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/links/2.0.1--h9f5acd7_2
$ module help quay.io/biocontainers/links/2.0.1--h9f5acd7_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### links-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### links-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### links-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### links-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### links-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### links-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LINKS

```bash
$ singularity exec <container> /usr/local/bin/LINKS
$ podman run --it --rm --entrypoint /usr/local/bin/LINKS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINKS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LINKS-make

```bash
$ singularity exec <container> /usr/local/bin/LINKS-make
$ podman run --it --rm --entrypoint /usr/local/bin/LINKS-make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINKS-make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LINKS-make-real

```bash
$ singularity exec <container> /usr/local/bin/LINKS-make-real
$ podman run --it --rm --entrypoint /usr/local/bin/LINKS-make-real   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINKS-make-real   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LINKS.pl

```bash
$ singularity exec <container> /usr/local/bin/LINKS.pl
$ podman run --it --rm --entrypoint /usr/local/bin/LINKS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINKS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LINKS_CPP

```bash
$ singularity exec <container> /usr/local/bin/LINKS_CPP
$ podman run --it --rm --entrypoint /usr/local/bin/LINKS_CPP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINKS_CPP   -v ${PWD} -w ${PWD} <container> -c " $@"
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