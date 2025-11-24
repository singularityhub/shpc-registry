---
layout: container
name:  "quay.io/biocontainers/pyfamsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyfamsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyfamsa/container.yaml"
updated_at: "2025-11-24 04:02:18.763045"
latest: "0.5.3--py310h8ea774a_1"
container_url: "https://biocontainers.pro/tools/pyfamsa"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2.0--py39h67e14b5_0"
 - "0.2.0--py310h068649b_2"
 - "0.3.0--py38hcbe9525_0"
 - "0.3.2--py38hcbe9525_0"
 - "0.3.2--py39he10ea66_1"
 - "0.2.0--py38hcbe9525_2"
 - "0.4.0--py38hcbe9525_0"
 - "0.4.0--py312h719dbc0_1"
 - "0.5.1--py312h719dbc0_0"
 - "0.5.2--py310hc31ed2c_0"
 - "0.5.3--py38hfe239e1_0"
 - "0.5.3--py310h8ea774a_1"
 - "0.5.3.post1--py312h9c9b0c2_0"
description: "singularity registry hpc automated addition for pyfamsa"
config: {"url": "https://biocontainers.pro/tools/pyfamsa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyfamsa", "latest": {"0.5.3--py310h8ea774a_1": "sha256:1e75b94f21d50a7db78323c51a0af70f5369f05a5530c43b39fc3df72af6b62b"}, "tags": {"0.2.0--py39h67e14b5_0": "sha256:1dc3ead7158b13c690e0a4128644047891f391742e3fa14976dbdbdf981bcef9", "0.2.0--py310h068649b_2": "sha256:50ff424e6e3099c22f2de308c6f312dfffb047bee1b940d43261a794c229087d", "0.3.0--py38hcbe9525_0": "sha256:635d470a56f28721db6055ef496be1092eea8b230ff4f460930e42b652fcf195", "0.3.2--py38hcbe9525_0": "sha256:56c3c894aa4c9797aec0fb264ec8383c32728bcb80f069bf5c9b4da197ebb663", "0.3.2--py39he10ea66_1": "sha256:47cf738f3387827a64571276ae70bdb68eb0472cc1a680c159af85baffb7cc14", "0.2.0--py38hcbe9525_2": "sha256:2099530ad69d52c339d4ee1fbac8c9fdc32aea16a30e72204fc3c3bb7e88f66e", "0.4.0--py38hcbe9525_0": "sha256:3b6af60e084cd6b257d7cdf94c286a8e0fbc8709858a4b98e48f94d9b4183a55", "0.4.0--py312h719dbc0_1": "sha256:d0a2106e44dc0313869cf2bde79564aa1e065817d2cc79660df14eab9a3034bb", "0.5.1--py312h719dbc0_0": "sha256:c81d0ee184d0cfd0c6d3b8518bb3e3e3d2e45d702562fa18bed10e280ac9761f", "0.5.2--py310hc31ed2c_0": "sha256:9c4cbbe73fac329d79ca1087765545ce58041485e4d133b413bc78383ca9ea65", "0.5.3--py38hfe239e1_0": "sha256:b9732a1361cf04e4418201f2a8277d10f7bb559f8b89877a6c05c99a4c937efb", "0.5.3--py310h8ea774a_1": "sha256:1e75b94f21d50a7db78323c51a0af70f5369f05a5530c43b39fc3df72af6b62b", "0.5.3.post1--py312h9c9b0c2_0": "sha256:7e0951a6965f542dc52483b66b34d7e30e14e5d57b9dced1a8f4db56d3592a43"}, "docker": "quay.io/biocontainers/pyfamsa", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyfamsa.
singularity registry hpc automated addition for pyfamsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyfamsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyfamsa:0.5.3--py310h8ea774a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyfamsa/0.5.3--py310h8ea774a_1
$ module help quay.io/biocontainers/pyfamsa/0.5.3--py310h8ea774a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyfamsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyfamsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyfamsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyfamsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyfamsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyfamsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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