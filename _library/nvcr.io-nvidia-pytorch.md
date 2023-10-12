---
layout: container
name:  "nvcr.io/nvidia/pytorch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/pytorch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/nvidia/pytorch/container.yaml"
updated_at: "2023-10-12 03:31:22.698406"
latest: "23.08-py3"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:pytorch/tags"

versions:
 - "21.02-py3"
 - "21.03-py3"
 - "21.04-py3"
 - "21.05-py3"
 - "21.06-py3"
 - "21.08-py3"
 - "21.10-py3"
 - "21.11-py3"
 - "21.12-py3"
 - "22.01-py3"
 - "22.02-py3"
 - "22.03-py3"
 - "22.04-py3"
 - "22.05-py3"
 - "22.06-py3"
 - "22.08-py3"
 - "22.07-py3"
 - "22.10-py3"
 - "22.09-py3"
 - "22.12-py3"
 - "22.11-py3"
 - "23.01-py3"
 - "23.02-py3"
 - "23.03-py3"
 - "23.04-py3"
 - "23.05-py3"
 - "23.06-py3"
 - "23.07-py3"
 - "23.08-py3"
description: "PyTorch is a GPU accelerated tensor computational framework with a Python front end. Functionality can be easily extended with common Python libraries such as NumPy, SciPy, and Cython. Automatic differentiation is done with a tape-based system at both a functional and neural network layer level."
config: {"docker": "nvcr.io/nvidia/pytorch", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:pytorch/tags", "maintainer": "@vsoch", "description": "PyTorch is a GPU accelerated tensor computational framework with a Python front end. Functionality can be easily extended with common Python libraries such as NumPy, SciPy, and Cython. Automatic differentiation is done with a tape-based system at both a functional and neural network layer level.", "latest": {"23.08-py3": "sha256:12a39f22d6e3a3cfcb285a238b6219475181672ff41a557a75bdeeef6d630740"}, "tags": {"21.02-py3": "sha256:d0fd1375f4c730a3fcff3b501856e087853fa627dc5c18649b72056b06c5ba03", "21.03-py3": "sha256:6aeffe9d0d90bdbb18185da71d2bfe2b4e73e3c506b678b5befc68214c2dbdcb", "21.04-py3": "sha256:27ae0df7f28d486bc38292dd818383cf465864837963612f549508a8ee25bdcc", "21.05-py3": "sha256:a5986639e4cf01eb35c0c0a9ca9fb9c6f905cc1b546966b78de4f69d15b894cf", "21.06-py3": "sha256:74a31ca4b89914fa0c23238514ec40d2322406826c7b9d99a437ed8c512da6e1", "21.08-py3": "sha256:2feee29307507dc51e1c0f10447ac897483682a747692c1c4d02cad52f59ab75", "21.10-py3": "sha256:267948c348eed1604ca180612d6a6ceb7298e4b0ee5900e2aee579edebb19caf", "21.11-py3": "sha256:417621e0d2a965d8030854d848eb48b2efa18d21e4c0959d71e01b58c1346e84", "21.12-py3": "sha256:a8da7de491196b61e06909c39bcccc0a1c5c4e0a89ecfb2d55a56164bafa9fc9", "22.01-py3": "sha256:06f27ba6699e079831943df12c6b537954377c9b2f84a569d1bf61b7ad164efa", "22.02-py3": "sha256:a66869fcfb7203ca6be9f793bc1f2dce946ed6569b728422db8503172542f574", "22.03-py3": "sha256:aba37c9ec089ce56e30686eafb535685ad31c53996b0e44626893e292157bf17", "22.04-py3": "sha256:49642d53129cef3b6b5cc0551e82ac98606c5ec6c4f6d3677ddc25bde1c82b88", "22.05-py3": "sha256:63ea06f4f74424fee3f3df4e6a0d26ce37211b0b7fb43e719c559ef970674c69", "22.06-py3": "sha256:6f9a1fdfcbc1d1aa6f28791ed7dc41d651d7c47d634c6a11b4f0692c50c8a664", "22.08-py3": "sha256:1aa83e1a13f756f31dabf82bc5a3c4f30ba423847cb230ce8c515f3add88b262", "22.07-py3": "sha256:f35ef66eaf03f437f041fad66e3e6edf9b107aedcc716d54011571e79b652d04", "22.10-py3": "sha256:7ad18fc3d2b9cdc35f9e5f0043987e8391fcf592c88177fdd9daa31b3b886be9", "22.09-py3": "sha256:ad07f7144606cb749dceb1ce7ed2286eeb69a63327ea7eccc69f0ac8ac1e0c68", "22.12-py3": "sha256:09a80f272dd173c9d8f28c23a1985aebe2bd3edd41a184ee9634f6e3f8a1f63d", "22.11-py3": "sha256:cbf761c3272cb0aadeec49aa188c3140ae79674e950cd0bb846b3683f93318be", "23.01-py3": "sha256:cbaa53e58a9f0aa8510fda7fba9e29ef5f14ca3ada280ce2ab601881a3cd9618", "23.02-py3": "sha256:8f28ac7d184cabe3acfdb00fb61197ba1618d8230e105dfc466ccdd78c521659", "23.03-py3": "sha256:6fffaca1c540d9871f97ac2459268bef566f7f73768768c47cacfaee810abe67", "23.04-py3": "sha256:5dd0caf52947719ba4fc170e779cfb20a5ecac7c91ca530f2884ed35fb97005f", "23.05-py3": "sha256:d5aa1e516e68afab9cd3ecaaeac3dd2178618bd26cd7ad96762ed53e32e9e0bd", "23.06-py3": "sha256:1b425aac0b20d47983412f8d2e348890c8087466af57de295c982b32ffdd26c8", "23.07-py3": "sha256:c53e8702a4ccb3f55235226dab29ef5d931a2a6d4d003ab47ca2e7e670f7922b", "23.08-py3": "sha256:12a39f22d6e3a3cfcb285a238b6219475181672ff41a557a75bdeeef6d630740"}, "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/pytorch.
PyTorch is a GPU accelerated tensor computational framework with a Python front end. Functionality can be easily extended with common Python libraries such as NumPy, SciPy, and Cython. Automatic differentiation is done with a tape-based system at both a functional and neural network layer level.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/pytorch
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/pytorch:23.08-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/pytorch/23.08-py3
$ module help nvcr.io/nvidia/pytorch/23.08-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pytorch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pytorch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pytorch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pytorch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pytorch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pytorch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pytorch

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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