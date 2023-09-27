---
layout: container
name:  "quay.io/biocontainers/snakeobjects"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakeobjects/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakeobjects/container.yaml"
updated_at: "2023-09-27 02:26:04.044676"
latest: "3.1.2--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/snakeobjects"
aliases:
 - "sobjects"
 - "plac_runner.py"
 - "yte"
 - "pulptest"
 - "cbc"
 - "clp"
 - "snakemake"
 - "snakemake-bash-completion"
 - "tabulate"
 - "jupyter-trust"
 - "jupyter"
versions:
 - "3.1.1--pyh5e36f6f_0"
 - "3.1.2--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for snakeobjects"
config: {"url": "https://biocontainers.pro/tools/snakeobjects", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakeobjects", "latest": {"3.1.2--pyh7cba7a3_0": "sha256:56cd2c93fcff8d602c13a3632e652f1849f00c86b3dcf71a340e50f4afe6ab29"}, "tags": {"3.1.1--pyh5e36f6f_0": "sha256:1d92811a3779c5c9c7ed9046b2b9a88f8a5694e481c1ac896efe0ec4f1021b04", "3.1.2--pyh7cba7a3_0": "sha256:56cd2c93fcff8d602c13a3632e652f1849f00c86b3dcf71a340e50f4afe6ab29"}, "docker": "quay.io/biocontainers/snakeobjects", "aliases": {"sobjects": "/usr/local/bin/sobjects", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "tabulate": "/usr/local/bin/tabulate", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakeobjects.
shpc-registry automated BioContainers addition for snakeobjects
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakeobjects
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakeobjects:3.1.2--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakeobjects/3.1.2--pyh7cba7a3_0
$ module help quay.io/biocontainers/snakeobjects/3.1.2--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakeobjects-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakeobjects-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakeobjects-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakeobjects-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakeobjects-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakeobjects-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sobjects

```bash
$ singularity exec <container> /usr/local/bin/sobjects
$ podman run --it --rm --entrypoint /usr/local/bin/sobjects   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sobjects   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter

```bash
$ singularity exec <container> /usr/local/bin/jupyter
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter   -v ${PWD} -w ${PWD} <container> -c " $@"
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