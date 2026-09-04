---
layout: container
name:  "quay.io/biocontainers/turboani"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/turboani/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/turboani/container.yaml"
updated_at: "2026-09-04 07:33:10.386729"
latest: "0.1.8--h39acb7c_0"
container_url: "https://biocontainers.pro/tools/turboani"
aliases:
 - "fastani"
 - "plot-correlation"
 - "turboani"
 - "fc-genconf"
versions:
 - "0.1.7--h39acb7c_0"
 - "0.1.8--h39acb7c_0"
description: "singularity registry hpc automated addition for turboani"
config: {"url": "https://biocontainers.pro/tools/turboani", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for turboani", "latest": {"0.1.8--h39acb7c_0": "sha256:429e2a28710a50c3bfbc6a9292bae3a0c575568fad4685ca6ca81ec47b376a4c"}, "tags": {"0.1.7--h39acb7c_0": "sha256:0697dd7c73781a214511d464a3d68980d344851c20b0537f80e960bf681255c5", "0.1.8--h39acb7c_0": "sha256:429e2a28710a50c3bfbc6a9292bae3a0c575568fad4685ca6ca81ec47b376a4c"}, "docker": "quay.io/biocontainers/turboani", "aliases": {"fastani": "/usr/local/bin/fastani", "plot-correlation": "/usr/local/bin/plot-correlation", "turboani": "/usr/local/bin/turboani", "fc-genconf": "/usr/local/bin/fc-genconf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/turboani.
singularity registry hpc automated addition for turboani
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/turboani
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/turboani:0.1.8--h39acb7c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/turboani/0.1.8--h39acb7c_0
$ module help quay.io/biocontainers/turboani/0.1.8--h39acb7c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### turboani-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### turboani-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### turboani-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### turboani-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### turboani-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### turboani-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastani

```bash
$ singularity exec <container> /usr/local/bin/fastani
$ podman run --it --rm --entrypoint /usr/local/bin/fastani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-correlation

```bash
$ singularity exec <container> /usr/local/bin/plot-correlation
$ podman run --it --rm --entrypoint /usr/local/bin/plot-correlation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-correlation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### turboani

```bash
$ singularity exec <container> /usr/local/bin/turboani
$ podman run --it --rm --entrypoint /usr/local/bin/turboani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/turboani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
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