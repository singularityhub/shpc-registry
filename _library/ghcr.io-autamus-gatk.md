---
layout: container
name:  "ghcr.io/autamus/gatk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gatk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/gatk/container.yaml"
updated_at: "2024-02-19 02:32:19.162234"
latest: "4.2.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/gatk"
aliases:
 - "gatk"
versions:
 - "4.2.0.0"
 - "4.2.2.0"
 - "4.2.3.0"
 - "latest"
 - "4.2.6.1"
description: "GATK (pronounced 'Gee-ay-tee-kay', not 'Gat-kay'), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery."
config: {"docker": "ghcr.io/autamus/gatk", "url": "https://github.com/orgs/autamus/packages/container/package/gatk", "maintainer": "@vsoch", "description": "GATK (pronounced 'Gee-ay-tee-kay', not 'Gat-kay'), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery.", "latest": {"4.2.3.0": "sha256:61adbb45a3a346cf987e56b49a5c9325d134a596a794b2a1569545205ecc296a"}, "tags": {"4.2.0.0": "sha256:1e46de1d7a1629f3c7c18cbd803cf1a06ddc36814a79a960f1e6128d35a71c9c", "4.2.2.0": "sha256:73b7c52cd78aceab6638a4734aefecdcaa800c9d46a79afb53da63b9ae6838b1", "4.2.3.0": "sha256:61adbb45a3a346cf987e56b49a5c9325d134a596a794b2a1569545205ecc296a", "latest": "sha256:e44c433847e7c9b8dbdade4b9a19f8f6d98ac66da2ff106252c6aaab1ddf4d2e", "4.2.6.1": "sha256:e44c433847e7c9b8dbdade4b9a19f8f6d98ac66da2ff106252c6aaab1ddf4d2e"}, "aliases": {"gatk": "/opt/view/bin/gatk"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gatk.
GATK (pronounced 'Gee-ay-tee-kay', not 'Gat-kay'), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gatk
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gatk:4.2.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gatk/4.2.3.0
$ module help ghcr.io/autamus/gatk/4.2.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gatk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gatk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gatk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gatk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gatk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gatk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gatk

```bash
$ singularity exec <container> /opt/view/bin/gatk
$ podman run --it --rm --entrypoint /opt/view/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
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