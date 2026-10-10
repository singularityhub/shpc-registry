---
layout: container
name:  "quay.io/biocontainers/reveal-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reveal-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reveal-tools/container.yaml"
updated_at: "2026-10-10 19:47:02.520789"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/reveal-tools"
aliases:
 - "REVEAL"
 - "hb-raster"
 - "hb-vector"
 - "fc-genconf"
 - "pandoc-lua"
 - "pandoc-server"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "x86_64-conda-linux-gnu.cfg"
 - "pandoc"
 - "numpy-config"
 - "hb-info"
versions:
 - "1.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for reveal-tools"
config: {"url": "https://biocontainers.pro/tools/reveal-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for reveal-tools", "latest": {"1.0.0--hdfd78af_0": "sha256:96663451b7ebb58826916c6b69428abd747d3fe806641ee410ea62d6fead1e0d"}, "tags": {"1.0.0--hdfd78af_0": "sha256:96663451b7ebb58826916c6b69428abd747d3fe806641ee410ea62d6fead1e0d"}, "docker": "quay.io/biocontainers/reveal-tools", "aliases": {"REVEAL": "/usr/local/bin/REVEAL", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "fc-genconf": "/usr/local/bin/fc-genconf", "pandoc-lua": "/usr/local/bin/pandoc-lua", "pandoc-server": "/usr/local/bin/pandoc-server", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "pandoc": "/usr/local/bin/pandoc", "numpy-config": "/usr/local/bin/numpy-config", "hb-info": "/usr/local/bin/hb-info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reveal-tools.
singularity registry hpc automated addition for reveal-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reveal-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reveal-tools:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reveal-tools/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/reveal-tools/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reveal-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reveal-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reveal-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reveal-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reveal-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reveal-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### REVEAL

```bash
$ singularity exec <container> /usr/local/bin/REVEAL
$ podman run --it --rm --entrypoint /usr/local/bin/REVEAL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REVEAL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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