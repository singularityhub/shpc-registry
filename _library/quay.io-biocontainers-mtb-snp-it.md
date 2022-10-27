---
layout: container
name:  "quay.io/biocontainers/mtb-snp-it"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mtb-snp-it/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mtb-snp-it/container.yaml"
updated_at: "2022-10-27 00:53:32.211718"
latest: "1.1--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/mtb-snp-it"
aliases:
 - "snpit-run.py"
versions:
 - "1.1--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for mtb-snp-it"
config: {"url": "https://biocontainers.pro/tools/mtb-snp-it", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mtb-snp-it", "latest": {"1.1--pyh864c0ab_1": "sha256:189a543689b0f6129e43950f4c156994b32e3c7d207f29cf622c595ff370e190"}, "tags": {"1.1--pyh864c0ab_1": "sha256:189a543689b0f6129e43950f4c156994b32e3c7d207f29cf622c595ff370e190"}, "docker": "quay.io/biocontainers/mtb-snp-it", "aliases": {"snpit-run.py": "/usr/local/bin/snpit-run.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mtb-snp-it.
shpc-registry automated BioContainers addition for mtb-snp-it
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mtb-snp-it
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mtb-snp-it:1.1--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mtb-snp-it/1.1--pyh864c0ab_1
$ module help quay.io/biocontainers/mtb-snp-it/1.1--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mtb-snp-it-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mtb-snp-it-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mtb-snp-it-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mtb-snp-it-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mtb-snp-it-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mtb-snp-it-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snpit-run.py

```bash
$ singularity exec <container> /usr/local/bin/snpit-run.py
$ podman run --it --rm --entrypoint /usr/local/bin/snpit-run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpit-run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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