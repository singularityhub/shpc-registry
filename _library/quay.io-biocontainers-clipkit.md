---
layout: container
name:  "quay.io/biocontainers/clipkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clipkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clipkit/container.yaml"
updated_at: "2025-12-08 03:51:44.717584"
latest: "2.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/clipkit"
aliases:
 - "clipkit"
 - "tqdm"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.3.0--pyhdfd78af_0"
 - "1.4.1--pyhdfd78af_0"
 - "2.0.1--pyhdfd78af_0"
 - "2.1.1--pyhdfd78af_0"
 - "2.3.0--pyhdfd78af_0"
 - "2.2.6--pyhdfd78af_0"
 - "2.1.3--pyhdfd78af_0"
 - "2.4.1--pyhdfd78af_0"
 - "2.6.1--pyhdfd78af_0"
 - "2.7.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for clipkit"
config: {"url": "https://biocontainers.pro/tools/clipkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clipkit", "latest": {"2.7.0--pyhdfd78af_0": "sha256:c074125d88620e088345c730b1fa572f3467cbf6b6441728262a4ee3b2a86c00"}, "tags": {"1.3.0--pyhdfd78af_0": "sha256:bb97e79f0e669a077bda8d2366dd583fbcbf4991d5396bdca4162896c351cd13", "1.4.1--pyhdfd78af_0": "sha256:0d4ad4d017b51085230d69c436407853fbd303b3edb528f3c164713d656c03ae", "2.0.1--pyhdfd78af_0": "sha256:3ec12c184e578cd7f3a73aada58088e2cf009d716cbd7eeb84c80a25b4e49780", "2.1.1--pyhdfd78af_0": "sha256:cf16f0df524779f63176aaf4474a70d61e1db363fafeae049d43dcf86752dc2a", "2.3.0--pyhdfd78af_0": "sha256:181ecbd2e56c13956c5b2702edffb03deb11381b687105a12452b1647184f3f7", "2.2.6--pyhdfd78af_0": "sha256:73a06053320f2ee037bfc65048cc724c4b4ed81ed502f25b4cd065883df72b2e", "2.1.3--pyhdfd78af_0": "sha256:41dfe2386aac85930ced8fdc3a6bf608d77751facf323b54b07621ad68633a8e", "2.4.1--pyhdfd78af_0": "sha256:821770a35e91f5d069e5beb5496891d1d4458ed8d377547035bda2400f964dfe", "2.6.1--pyhdfd78af_0": "sha256:e6f0cb50d1d276c93b2f8010e4b7908e1947c4620ff2525e287f15ce107b9ece", "2.7.0--pyhdfd78af_0": "sha256:c074125d88620e088345c730b1fa572f3467cbf6b6441728262a4ee3b2a86c00"}, "docker": "quay.io/biocontainers/clipkit", "aliases": {"clipkit": "/usr/local/bin/clipkit", "tqdm": "/usr/local/bin/tqdm", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clipkit.
shpc-registry automated BioContainers addition for clipkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clipkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clipkit:2.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clipkit/2.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/clipkit/2.7.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clipkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clipkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clipkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clipkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clipkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clipkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clipkit

```bash
$ singularity exec <container> /usr/local/bin/clipkit
$ podman run --it --rm --entrypoint /usr/local/bin/clipkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clipkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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