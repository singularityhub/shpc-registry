---
layout: container
name:  "quay.io/biocontainers/mess"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mess/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mess/container.yaml"
updated_at: "2024-12-15 03:46:26.169516"
latest: "0.10.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mess"
aliases:
 - "mess"
 - "pulptest"
 - "cbc"
 - "clp"
 - "snakemake"
 - "snakemake-bash-completion"
 - "jupyter-trust"
 - "jupyter"
 - "jupyter-migrate"
 - "jupyter-troubleshoot"
 - "rst2html4.py"
versions:
 - "v0.2.1--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.8.2--pyhdfd78af_0"
 - "0.8.3--pyhdfd78af_0"
 - "0.9.0--pyhdfd78af_0"
 - "0.8.3--pyhdfd78af_1"
 - "0.9.0--pyhdfd78af_1"
 - "0.10.0--pyhdfd78af_0"
 - "0.9.0--pyhdfd78af_2"
description: "shpc-registry automated BioContainers addition for mess"
config: {"url": "https://biocontainers.pro/tools/mess", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mess", "latest": {"0.10.0--pyhdfd78af_0": "sha256:2b8845546facf6edcf161e7e4c5e11078efe5d15efa41cf711450e2e22fe70b7"}, "tags": {"v0.2.1--pyhdfd78af_0": "sha256:075b9a2353137cadffd70344aa01537de415419bf09a66eee659d674b4c1f581", "0.2.2--pyhdfd78af_0": "sha256:1d07b5dd14e16bef7001b9a95e1c3141ee543b42c806c97271e9dba22d570c74", "0.8.2--pyhdfd78af_0": "sha256:4010dab1edfb9397a29950a8bb31bd7cf85b70c237435693080ae31b029e23c4", "0.8.3--pyhdfd78af_0": "sha256:bad8c2def7b642ea1d220964d2926d3eb42e734caa1bb720c8185c57c2dc0f83", "0.9.0--pyhdfd78af_0": "sha256:1e70b244495418f6fb1a8ec8ca34ed67750e367d692e6f705927b0a932bbb4a6", "0.8.3--pyhdfd78af_1": "sha256:6bfe5ae7647a45e0a18f64c5cfb275b61f2e0f82bb2fad8ecf427385b13d373d", "0.9.0--pyhdfd78af_1": "sha256:2c354d0b9e83f43c0506257db3c2a8045fe6b0db27e8ebcb92efe1eae6725f9a", "0.10.0--pyhdfd78af_0": "sha256:2b8845546facf6edcf161e7e4c5e11078efe5d15efa41cf711450e2e22fe70b7", "0.9.0--pyhdfd78af_2": "sha256:060bd2df81e1c9054287a35611a5736255e6b4ec5e52dd0ee5ff170979cd1766"}, "docker": "quay.io/biocontainers/mess", "aliases": {"mess": "/usr/local/bin/mess", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "jupyter-trust": "/usr/local/bin/jupyter-trust", "jupyter": "/usr/local/bin/jupyter", "jupyter-migrate": "/usr/local/bin/jupyter-migrate", "jupyter-troubleshoot": "/usr/local/bin/jupyter-troubleshoot", "rst2html4.py": "/usr/local/bin/rst2html4.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mess.
shpc-registry automated BioContainers addition for mess
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mess
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mess:0.10.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mess/0.10.0--pyhdfd78af_0
$ module help quay.io/biocontainers/mess/0.10.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mess-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mess-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mess-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mess-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mess-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mess-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mess

```bash
$ singularity exec <container> /usr/local/bin/mess
$ podman run --it --rm --entrypoint /usr/local/bin/mess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mess   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jupyter-migrate

```bash
$ singularity exec <container> /usr/local/bin/jupyter-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-troubleshoot

```bash
$ singularity exec <container> /usr/local/bin/jupyter-troubleshoot
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-troubleshoot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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