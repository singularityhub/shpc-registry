---
layout: container
name:  "quay.io/biocontainers/enhjoerning"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enhjoerning/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enhjoerning/container.yaml"
updated_at: "2025-11-14 03:29:26.058554"
latest: "2.3.0--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/enhjoerning"
aliases:
 - "unicorn"
 - "ref-cache"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.0.2--h577a1d6_0"
 - "2.0.3--h577a1d6_0"
 - "2.2.0--h577a1d6_0"
 - "2.1.0--h577a1d6_0"
 - "2.3.0--h577a1d6_0"
description: "singularity registry hpc automated addition for enhjoerning"
config: {"url": "https://biocontainers.pro/tools/enhjoerning", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for enhjoerning", "latest": {"2.3.0--h577a1d6_0": "sha256:1b2028c9c2726e0e874934e12fb2a7b5b19c8cb7919e3a6bf3c33781c4b7e909"}, "tags": {"2.0.2--h577a1d6_0": "sha256:8535e7493b746b2631ee72077ee6cffd36e821fe0e1dc1b40a336b7de752edd1", "2.0.3--h577a1d6_0": "sha256:ab3bf169c27fe29134f87ecfb8cda9d308c6a6d3e1b5af22636072063adfa177", "2.2.0--h577a1d6_0": "sha256:6e1b079f15c79d571aff22e9218e80abaa2138284f653daa9e5d30299ddeaafe", "2.1.0--h577a1d6_0": "sha256:e17edf32921910acaef7088b7a1c85fac2890e7f568061f4e8d50fd792ff6f02", "2.3.0--h577a1d6_0": "sha256:1b2028c9c2726e0e874934e12fb2a7b5b19c8cb7919e3a6bf3c33781c4b7e909"}, "docker": "quay.io/biocontainers/enhjoerning", "aliases": {"unicorn": "/usr/local/bin/unicorn", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enhjoerning.
singularity registry hpc automated addition for enhjoerning
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enhjoerning
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enhjoerning:2.3.0--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enhjoerning/2.3.0--h577a1d6_0
$ module help quay.io/biocontainers/enhjoerning/2.3.0--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enhjoerning-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enhjoerning-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enhjoerning-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enhjoerning-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enhjoerning-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enhjoerning-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unicorn

```bash
$ singularity exec <container> /usr/local/bin/unicorn
$ podman run --it --rm --entrypoint /usr/local/bin/unicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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