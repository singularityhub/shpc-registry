---
layout: container
name:  "quay.io/biocontainers/crisprme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crisprme/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/crisprme/container.yaml"
updated_at: "2022-10-27 01:14:09.074458"
latest: "1.6.8--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/crisprme"
aliases:
 - "crispritz.py"
 - "crisprme.py"
 - "dash-generate-components"
 - "gunicorn"
 - "renderer"
versions:
 - "1.6.8--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for crisprme"
config: {"url": "https://biocontainers.pro/tools/crisprme", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crisprme", "latest": {"1.6.8--hdfd78af_0": "sha256:10b29b3dc7beee5957972f5221f83e5155bd07b3b11387366d3bc55b313a0adf"}, "tags": {"1.6.8--hdfd78af_0": "sha256:10b29b3dc7beee5957972f5221f83e5155bd07b3b11387366d3bc55b313a0adf"}, "docker": "quay.io/biocontainers/crisprme", "aliases": {"crispritz.py": "/usr/local/bin/crispritz.py", "crisprme.py": "/usr/local/bin/crisprme.py", "dash-generate-components": "/usr/local/bin/dash-generate-components", "gunicorn": "/usr/local/bin/gunicorn", "renderer": "/usr/local/bin/renderer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crisprme.
shpc-registry automated BioContainers addition for crisprme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crisprme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crisprme:1.6.8--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crisprme/1.6.8--hdfd78af_0
$ module help quay.io/biocontainers/crisprme/1.6.8--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crisprme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crisprme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crisprme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crisprme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crisprme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crisprme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crispritz.py

```bash
$ singularity exec <container> /usr/local/bin/crispritz.py
$ podman run --it --rm --entrypoint /usr/local/bin/crispritz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crispritz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crisprme.py

```bash
$ singularity exec <container> /usr/local/bin/crisprme.py
$ podman run --it --rm --entrypoint /usr/local/bin/crisprme.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crisprme.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunicorn

```bash
$ singularity exec <container> /usr/local/bin/gunicorn
$ podman run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
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