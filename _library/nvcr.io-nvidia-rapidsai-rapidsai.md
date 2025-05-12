---
layout: container
name:  "nvcr.io/nvidia/rapidsai/rapidsai"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/rapidsai/rapidsai/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/nvidia/rapidsai/rapidsai/container.yaml"
updated_at: "2025-05-12 03:15:47.770875"
latest: "23.06-cuda11.8-runtime-ubuntu22.04-py3.10"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai/tags"
aliases:
 - "python"
versions:
 - "0.18-cuda11.0-runtime-centos7"
 - "22.02-cuda11.5-runtime-ubuntu20.04"
 - "21.10-cuda11.2-runtime-ubuntu20.04"
 - "21.08-cuda11.2-runtime-ubuntu20.04"
 - "21.06-cuda11.2-runtime-ubuntu20.04"
 - "cuda11.5-runtime-ubuntu20.04"
 - "22.04-cuda11.5-runtime-ubuntu20.04"
 - "22.06-cuda11.5-runtime-ubuntu20.04-py3.9"
 - "22.08-cuda11.5-runtime-ubuntu20.04-py3.9"
 - "22.10-cuda11.5-runtime-ubuntu20.04-py3.9"
 - "22.12-cuda11.5-runtime-ubuntu20.04-py3.9"
 - "23.02-cuda11.8-runtime-ubuntu22.04-py3.10"
 - "23.04-cuda11.8-runtime-ubuntu22.04-py3.10"
 - "23.06-cuda11.8-runtime-ubuntu22.04-py3.10"
description: "The RAPIDS suite of software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs."
config: {"docker": "nvcr.io/nvidia/rapidsai/rapidsai", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai/tags", "maintainer": "@vsoch", "description": "The RAPIDS suite of software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs.", "latest": {"23.06-cuda11.8-runtime-ubuntu22.04-py3.10": "sha256:a6fe9eca90aa6b71c840f91454c58f05d7ef4c24500da8493b62e96b42e5b3ee"}, "tags": {"0.18-cuda11.0-runtime-centos7": "sha256:9491e49936e10fc6e7c5b90a1d8141bab74e5879e1681146f0d2cf9aa6a9d24a", "22.02-cuda11.5-runtime-ubuntu20.04": "sha256:961282c653419d174ba496b023e27c9535b475c949947343ceda0b8e8baea64a", "21.10-cuda11.2-runtime-ubuntu20.04": "sha256:16d8ea2a5e15e3157986082b091462477fee0216e805e11626db7abd4b582cd7", "21.08-cuda11.2-runtime-ubuntu20.04": "sha256:c4508c3862e47432f28f11bad12d19493103928098b8e3d4c6e92a93115e6efb", "21.06-cuda11.2-runtime-ubuntu20.04": "sha256:e28506f37088fbd9bb24356f9ebbbe40553dd4898127f0fe7d8c145b61fed736", "cuda11.5-runtime-ubuntu20.04": "sha256:8a2c14908d12558e1e1d96950bb032c6e54563aa0faa73ae112d2e602aff6def", "22.04-cuda11.5-runtime-ubuntu20.04": "sha256:8a2c14908d12558e1e1d96950bb032c6e54563aa0faa73ae112d2e602aff6def", "22.06-cuda11.5-runtime-ubuntu20.04-py3.9": "sha256:bbe4fc5eb916f9e1c26b885f5586335b86fbbbc9fb8e8f19d2429ab4a79aa0fd", "22.08-cuda11.5-runtime-ubuntu20.04-py3.9": "sha256:c6ee5a8ee321719694fe23087ec6911e6d21effe2fa7fdc9bdf39ccf63e94cd5", "22.10-cuda11.5-runtime-ubuntu20.04-py3.9": "sha256:f40c36559f255c728f5e616c67fbeb28494ea69f565867bf833aef13cf8f4f80", "22.12-cuda11.5-runtime-ubuntu20.04-py3.9": "sha256:f45f17599a44d9ba602e5157b7bf4dc1e7cfd1fda83cbea4355a04989ee5a5a0", "23.02-cuda11.8-runtime-ubuntu22.04-py3.10": "sha256:23cca281fe69511ff194bd5c76ce306e9237ab21d91ca8fff7a47930ac3cbb38", "23.04-cuda11.8-runtime-ubuntu22.04-py3.10": "sha256:a6aa67b19a65e0d1f35a18558ecb05efbe28d04afa92cc9b5e17c56cdc479e8c", "23.06-cuda11.8-runtime-ubuntu22.04-py3.10": "sha256:a6fe9eca90aa6b71c840f91454c58f05d7ef4c24500da8493b62e96b42e5b3ee"}, "filter": ["^((?!base).)*$"], "aliases": {"python": "/opt/conda/bin/python"}, "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/rapidsai/rapidsai.
The RAPIDS suite of software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/rapidsai/rapidsai
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/rapidsai/rapidsai:23.06-cuda11.8-runtime-ubuntu22.04-py3.10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/rapidsai/rapidsai/23.06-cuda11.8-runtime-ubuntu22.04-py3.10
$ module help nvcr.io/nvidia/rapidsai/rapidsai/23.06-cuda11.8-runtime-ubuntu22.04-py3.10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapidsai-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapidsai-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapidsai-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapidsai-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapidsai-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapidsai-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /opt/conda/bin/python
$ podman run --it --rm --entrypoint /opt/conda/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/conda/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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