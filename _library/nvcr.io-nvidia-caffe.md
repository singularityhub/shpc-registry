---
layout: container
name:  "nvcr.io/nvidia/caffe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/caffe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/nvidia/caffe/container.yaml"
updated_at: "2023-11-20 03:14:13.256760"
latest: "sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:caffe/tags"
aliases:
 - "python"
versions:
 - "20.03-py3"
 - "sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex"
 - "sha256-95740df9a299abcb4fccb1870486228aad0d0ccffa45096f1ff25db5128eeda6.sbom"
 - "sha256-abac68858dfe093781086726a0b58ceedf78198adbdac5c0ed2c1eec118e5f13.vex"
 - "sha256-24610de52c7600d87b56f8e807707de6f8e8a7e6e28110bef0f6cd7c9a6ffd84.sbom"
 - "sha256-23084ea6556538c70c60348e3623f921e4c299f0e6da11deb94e63a15ced7892.vex"
description: "NVIDIA Caffe, also known as NVCaffe, is an NVIDIA-maintained fork of Berkeley Vision and Learning Center (BVLC) Caffe tuned for NVIDIA GPUs, particularly in multi-GPU configurations."
config: {"docker": "nvcr.io/nvidia/caffe", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:caffe/tags", "maintainer": "@vsoch", "description": "NVIDIA Caffe, also known as NVCaffe, is an NVIDIA-maintained fork of Berkeley Vision and Learning Center (BVLC) Caffe tuned for NVIDIA GPUs, particularly in multi-GPU configurations.", "latest": {"sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex": "sha256:4c9f2f014706b4775293e9260c814bb44896dba42081e1fdbd99d9e77f01a5e1"}, "tags": {"20.03-py3": "sha256:c6fb6d8309be4c43ccdc7dd19dde73d186404df3627f660866178eff507e22c7", "sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex": "sha256:4c9f2f014706b4775293e9260c814bb44896dba42081e1fdbd99d9e77f01a5e1", "sha256-95740df9a299abcb4fccb1870486228aad0d0ccffa45096f1ff25db5128eeda6.sbom": "sha256:f596f2cfa075cbd417d621be9656b1cfcce7c3820a17ebe51e5a3ac04d506341", "sha256-abac68858dfe093781086726a0b58ceedf78198adbdac5c0ed2c1eec118e5f13.vex": "sha256:6603cc6b3467b059044a5784e2d7eb75fec8e5303590919ae909753c907cb1a5", "sha256-24610de52c7600d87b56f8e807707de6f8e8a7e6e28110bef0f6cd7c9a6ffd84.sbom": "sha256:b3ff796893b7950278575c3e9ffbbb4753962eeb7ecad6988838a41386b2d0b7", "sha256-23084ea6556538c70c60348e3623f921e4c299f0e6da11deb94e63a15ced7892.vex": "sha256:1e8db7a816c23bbe058f661a3abfb54352c3494d18c3c32bbcb974d38003ed08"}, "aliases": {"python": "/usr/bin/python"}, "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/caffe.
NVIDIA Caffe, also known as NVCaffe, is an NVIDIA-maintained fork of Berkeley Vision and Learning Center (BVLC) Caffe tuned for NVIDIA GPUs, particularly in multi-GPU configurations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/caffe
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/caffe:sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/caffe/sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex
$ module help nvcr.io/nvidia/caffe/sha256-a99330afb47f4ae48e39b03bc50413031e42af39227155aa112c94f702597421.vex
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### caffe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### caffe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### caffe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### caffe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### caffe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### caffe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /usr/bin/python
$ podman run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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