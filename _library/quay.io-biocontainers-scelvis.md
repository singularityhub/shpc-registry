---
layout: container
name:  "quay.io/biocontainers/scelvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scelvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scelvis/container.yaml"
updated_at: "2025-12-29 04:53:34.324458"
latest: "0.8.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scelvis"
aliases:
 - "dash-generate-components"
 - "dash-update-components"
 - "rehttpfs"
 - "renderer"
 - "scelvis"
 - "scanpy"
 - "docutils"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "flask"
 - "pybabel"
 - "jp.py"
 - "numba"
versions:
 - "0.8.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scelvis"
config: {"url": "https://biocontainers.pro/tools/scelvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scelvis", "latest": {"0.8.9--pyhdfd78af_0": "sha256:271d44f615064690926fd914cf0fbca1ba74746c79cf7ac72eac71c59218943e"}, "tags": {"0.8.9--pyhdfd78af_0": "sha256:271d44f615064690926fd914cf0fbca1ba74746c79cf7ac72eac71c59218943e"}, "docker": "quay.io/biocontainers/scelvis", "aliases": {"dash-generate-components": "/usr/local/bin/dash-generate-components", "dash-update-components": "/usr/local/bin/dash-update-components", "rehttpfs": "/usr/local/bin/rehttpfs", "renderer": "/usr/local/bin/renderer", "scelvis": "/usr/local/bin/scelvis", "scanpy": "/usr/local/bin/scanpy", "docutils": "/usr/local/bin/docutils", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "flask": "/usr/local/bin/flask", "pybabel": "/usr/local/bin/pybabel", "jp.py": "/usr/local/bin/jp.py", "numba": "/usr/local/bin/numba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scelvis.
shpc-registry automated BioContainers addition for scelvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scelvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scelvis:0.8.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scelvis/0.8.9--pyhdfd78af_0
$ module help quay.io/biocontainers/scelvis/0.8.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scelvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scelvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scelvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scelvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scelvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scelvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dash-generate-components

```bash
$ singularity exec <container> /usr/local/bin/dash-generate-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-generate-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dash-update-components

```bash
$ singularity exec <container> /usr/local/bin/dash-update-components
$ podman run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dash-update-components   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rehttpfs

```bash
$ singularity exec <container> /usr/local/bin/rehttpfs
$ podman run --it --rm --entrypoint /usr/local/bin/rehttpfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rehttpfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renderer

```bash
$ singularity exec <container> /usr/local/bin/renderer
$ podman run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renderer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scelvis

```bash
$ singularity exec <container> /usr/local/bin/scelvis
$ podman run --it --rm --entrypoint /usr/local/bin/scelvis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scelvis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
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