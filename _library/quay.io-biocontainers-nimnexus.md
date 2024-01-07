---
layout: container
name:  "quay.io/biocontainers/nimnexus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nimnexus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nimnexus/container.yaml"
updated_at: "2024-01-07 02:33:54.291551"
latest: "0.1.1--hf43ccf4_4"
container_url: "https://biocontainers.pro/tools/nimnexus"
aliases:
 - "nimnexus"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1.1--hcb20899_3"
 - "0.1.1--hf43ccf4_4"
description: "shpc-registry automated BioContainers addition for nimnexus"
config: {"url": "https://biocontainers.pro/tools/nimnexus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nimnexus", "latest": {"0.1.1--hf43ccf4_4": "sha256:53c7378fdab7125b1e5a12366ff88735700a2cc09fa7af0fa56dbf5628006d03"}, "tags": {"0.1.1--hcb20899_3": "sha256:3a3e07cb246460cfda10bb119a4a1964d626fbe8d0541edd83d9b37f6ee3f867", "0.1.1--hf43ccf4_4": "sha256:53c7378fdab7125b1e5a12366ff88735700a2cc09fa7af0fa56dbf5628006d03"}, "docker": "quay.io/biocontainers/nimnexus", "aliases": {"nimnexus": "/usr/local/bin/nimnexus", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nimnexus.
shpc-registry automated BioContainers addition for nimnexus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nimnexus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nimnexus:0.1.1--hf43ccf4_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nimnexus/0.1.1--hf43ccf4_4
$ module help quay.io/biocontainers/nimnexus/0.1.1--hf43ccf4_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nimnexus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nimnexus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nimnexus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nimnexus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nimnexus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nimnexus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nimnexus

```bash
$ singularity exec <container> /usr/local/bin/nimnexus
$ podman run --it --rm --entrypoint /usr/local/bin/nimnexus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nimnexus   -v ${PWD} -w ${PWD} <container> -c " $@"
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