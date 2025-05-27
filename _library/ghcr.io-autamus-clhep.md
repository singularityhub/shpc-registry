---
layout: container
name:  "ghcr.io/autamus/clhep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/clhep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/clhep/container.yaml"
updated_at: "2025-05-27 19:52:23.666471"
latest: "2.4.5.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/clhep"
aliases:
 - "Cast-config"
 - "Evaluator-config"
 - "Exceptions-config"
 - "GenericFunctions-config"
 - "Geometry-config"
 - "Matrix-config"
 - "Random-config"
 - "RandomObjects-config"
 - "RefCount-config"
 - "Units-config"
 - "Utility-config"
 - "Vector-config"
 - "clhep-config"
versions:
 - "2.4.4.0"
 - "2.4.5.1"
 - "latest"
 - "2.4.6.0"
description: "CLHEP is a C++ library that provides utility classes for general numerical programming, vector arithmetic, geometry, pseudorandom number generation, and linear algebra, specifically targeted for high energy physics simulation and analysis software."
config: {"docker": "ghcr.io/autamus/clhep", "url": "https://github.com/orgs/autamus/packages/container/package/clhep", "maintainer": "@vsoch", "description": "CLHEP is a C++ library that provides utility classes for general numerical programming, vector arithmetic, geometry, pseudorandom number generation, and linear algebra, specifically targeted for high energy physics simulation and analysis software.", "latest": {"2.4.5.1": "sha256:5e73148f9fa144fc6333db76b27e176f73b2a99fc973d162ea589220c1fa543a"}, "tags": {"2.4.4.0": "sha256:b881d89a14929d265f8848ea9785bb8fea149c40e3aa1d471642b5268d3c02db", "2.4.5.1": "sha256:5e73148f9fa144fc6333db76b27e176f73b2a99fc973d162ea589220c1fa543a", "latest": "sha256:4b636e45637263a392f7ba30ff8b980c5148d2b522597618d3f70ae701884b18", "2.4.6.0": "sha256:4b636e45637263a392f7ba30ff8b980c5148d2b522597618d3f70ae701884b18"}, "aliases": {"Cast-config": "/opt/view/bin/Cast-config", "Evaluator-config": "/opt/view/bin/Evaluator-config", "Exceptions-config": "/opt/view/bin/Exceptions-config", "GenericFunctions-config": "/opt/view/bin/GenericFunctions-config", "Geometry-config": "/opt/view/bin/Geometry-config", "Matrix-config": "/opt/view/bin/Matrix-config", "Random-config": "/opt/view/bin/Random-config", "RandomObjects-config": "/opt/view/bin/RandomObjects-config", "RefCount-config": "/opt/view/bin/RefCount-config", "Units-config": "/opt/view/bin/Units-config", "Utility-config": "/opt/view/bin/Utility-config", "Vector-config": "/opt/view/bin/Vector-config", "clhep-config": "/opt/view/bin/clhep-config"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/clhep.
CLHEP is a C++ library that provides utility classes for general numerical programming, vector arithmetic, geometry, pseudorandom number generation, and linear algebra, specifically targeted for high energy physics simulation and analysis software.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/clhep
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/clhep:2.4.5.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/clhep/2.4.5.1
$ module help ghcr.io/autamus/clhep/2.4.5.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clhep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clhep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clhep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clhep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clhep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clhep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cast-config

```bash
$ singularity exec <container> /opt/view/bin/Cast-config
$ podman run --it --rm --entrypoint /opt/view/bin/Cast-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Cast-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Evaluator-config

```bash
$ singularity exec <container> /opt/view/bin/Evaluator-config
$ podman run --it --rm --entrypoint /opt/view/bin/Evaluator-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Evaluator-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Exceptions-config

```bash
$ singularity exec <container> /opt/view/bin/Exceptions-config
$ podman run --it --rm --entrypoint /opt/view/bin/Exceptions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Exceptions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenericFunctions-config

```bash
$ singularity exec <container> /opt/view/bin/GenericFunctions-config
$ podman run --it --rm --entrypoint /opt/view/bin/GenericFunctions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/GenericFunctions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Geometry-config

```bash
$ singularity exec <container> /opt/view/bin/Geometry-config
$ podman run --it --rm --entrypoint /opt/view/bin/Geometry-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Geometry-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Matrix-config

```bash
$ singularity exec <container> /opt/view/bin/Matrix-config
$ podman run --it --rm --entrypoint /opt/view/bin/Matrix-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Matrix-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Random-config

```bash
$ singularity exec <container> /opt/view/bin/Random-config
$ podman run --it --rm --entrypoint /opt/view/bin/Random-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Random-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RandomObjects-config

```bash
$ singularity exec <container> /opt/view/bin/RandomObjects-config
$ podman run --it --rm --entrypoint /opt/view/bin/RandomObjects-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/RandomObjects-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RefCount-config

```bash
$ singularity exec <container> /opt/view/bin/RefCount-config
$ podman run --it --rm --entrypoint /opt/view/bin/RefCount-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/RefCount-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Units-config

```bash
$ singularity exec <container> /opt/view/bin/Units-config
$ podman run --it --rm --entrypoint /opt/view/bin/Units-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Units-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Utility-config

```bash
$ singularity exec <container> /opt/view/bin/Utility-config
$ podman run --it --rm --entrypoint /opt/view/bin/Utility-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Utility-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vector-config

```bash
$ singularity exec <container> /opt/view/bin/Vector-config
$ podman run --it --rm --entrypoint /opt/view/bin/Vector-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Vector-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhep-config

```bash
$ singularity exec <container> /opt/view/bin/clhep-config
$ podman run --it --rm --entrypoint /opt/view/bin/clhep-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/clhep-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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