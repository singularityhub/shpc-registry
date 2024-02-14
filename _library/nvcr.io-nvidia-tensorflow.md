---
layout: container
name:  "nvcr.io/nvidia/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/nvidia/tensorflow/container.yaml"
updated_at: "2024-02-14 02:22:24.712201"
latest: "23.09-tf2-py3"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow/tags"

versions:
 - "21.02-tf1-py3"
 - "21.03-tf1-py3"
 - "21.04-tf1-py3"
 - "21.05-tf1-py3"
 - "21.06-tf1-py3"
 - "21.08-tf1-py3"
 - "21.10-tf1-py3"
 - "21.11-tf1-py3"
 - "21.12-tf1-py3"
 - "22.03-tf2-py3"
 - "22.02-tf2-py3"
 - "22.01-tf2-py3"
 - "21.12-tf2-py3"
 - "21.11-tf2-py3"
 - "22.04-tf2-py3"
 - "22.05-tf2-py3"
 - "22.06-tf2-py3"
 - "22.08-tf2-py3"
 - "22.07-tf2-py3"
 - "22.10-tf2-py3"
 - "22.09-tf2-py3"
 - "22.11-tf2-py3"
 - "22.12-tf2-py3"
 - "23.01-tf2-py3"
 - "23.02-tf2-py3"
 - "23.03-tf2-py3"
 - "23.04-tf2-py3"
 - "23.05-tf2-py3"
 - "23.06-tf2-py3"
 - "23.07-tf2-py3"
 - "23.08-tf2-py3"
 - "23.09-tf2-py3"
description: "TensorFlow is an open-source software library for high-performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices."
config: {"docker": "nvcr.io/nvidia/tensorflow", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow/tags", "maintainer": "@vsoch", "description": "TensorFlow is an open-source software library for high-performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices.", "latest": {"23.09-tf2-py3": "sha256:ddc195f339a7eadc648b0bf17bed974a8d50043616af1c919a2fb8ba2dd0fc2f"}, "tags": {"21.02-tf1-py3": "sha256:74f3e5f4a60a312df811ee5104baa189d158697953a91e7768f777895bb1d438", "21.03-tf1-py3": "sha256:addbbdccb193849d58083154458318b2aa9b7945d9975284291b08b4336415e1", "21.04-tf1-py3": "sha256:fb948e24013e079fbba954dc0ce025d3648d8b12d343cd07d24e7ca14b66ba5b", "21.05-tf1-py3": "sha256:a6a89e9ac5db5e67434785268b52df2a06df2fb437eed2abaf54df06db5e4f78", "21.06-tf1-py3": "sha256:e7248bb1c64f9d9bba0eae2906f7dc64efc8bd6b775915268a8b8e215f5a5850", "21.08-tf1-py3": "sha256:63d4ee297a200b7e3f28acad2dc7ce91b48ca2388d0aaa6c9996a6676b7c8fac", "21.10-tf1-py3": "sha256:d0735da72fff9c1e789c1cbc10a0ff7df7b08271236c667486f9cc7699da6e3d", "21.11-tf1-py3": "sha256:91efc28e1f304f8989c344a8cf7e4e06ac85d1ea1388d57480d3dabae60bf365", "21.12-tf1-py3": "sha256:315f7b44486b59d642ab6b52d626aa66ec432f8a4bf7eb793acc4e47af6ab165", "22.03-tf2-py3": "sha256:bafc7d96a17aab5bbc6f6aed0d2c44d2bcff05148fc9680741a0f2d4fb750420", "22.02-tf2-py3": "sha256:d1e40b32306d3f517da1c249972254f193d6a860e2383f393acbe719e74c13fb", "22.01-tf2-py3": "sha256:64274c3f12592c37ee57f839981d18c046be399a41fd234caedacd9d803d15f4", "21.12-tf2-py3": "sha256:afb70040bc7982a7b23219a6a71298c76904e1a815ea70203f1b52d8a8dad65b", "21.11-tf2-py3": "sha256:03e12291e8a03aaf70d0cba6ae994b9738b79f4b939bfe4d416ea3e53027bbad", "22.04-tf2-py3": "sha256:c7450cdb0fb3737411f415b89e1866547317b757db8db85c30a0fd58becc2ef0", "22.05-tf2-py3": "sha256:f57af74cd8bb2145f649fb440dc6231986f1c6fd2ccedaeaee8995b5f3be2389", "22.06-tf2-py3": "sha256:ea76aabaa17ee0e308a443fa1e7666f98350865f266b02610a60791bd0feeb40", "22.08-tf2-py3": "sha256:b4db3bfef51088131142ab9379969a70c085b514399a04643d5af28e2d3c2852", "22.07-tf2-py3": "sha256:5ceb426d476b0c24104fd8b036d6c8f7ef0d1579b133f53158f891861cddab1f", "22.10-tf2-py3": "sha256:43cba5f7af3df606836e80e28676db111cc95a812e063d0c9a9f47b791a8fb31", "22.09-tf2-py3": "sha256:557d3b551e5b9dba53014a09fc6af2d0a97bfd871b47aa0027c8d992c4f4ccec", "22.11-tf2-py3": "sha256:9546a59d4eb6a4517f843bdf61a7e7279621ca4c2c74fb0da5f59c99dff3d259", "22.12-tf2-py3": "sha256:947e32a2649f805bc5159b4fbb9cd70111fc60d3129ccee595d50435df318a92", "23.01-tf2-py3": "sha256:e760ec46b2d13bc9e5b076fab69aec680287173ea1b532a19dbc00e76f8faa3f", "23.02-tf2-py3": "sha256:14b48be2c853407dd7a4a548d31348cb15a1eed369a6410f09a11ddd52d4b6d0", "23.03-tf2-py3": "sha256:e8ec1f070d9ed926c4c08e1faec0652c3442986491297259251908e9bb2688a8", "23.04-tf2-py3": "sha256:7d076c2420bfe5085e642d66f1ce13391a23714dbe05b37ad73cee79226c2f4c", "23.05-tf2-py3": "sha256:85f0ff81580cd644c0893e8c66ac768c4c3d09a59de8025927078fbb584aa73b", "23.06-tf2-py3": "sha256:11a010d10bde236da61970ea8ce6a1d0f7ac57c25129cf36839654c58cf146bf", "23.07-tf2-py3": "sha256:e33c842c79c3c010191df409dc561ccf99c5465e13e4a82a4419fadb1740e37e", "23.08-tf2-py3": "sha256:76fe2dad037a179f73707b23d164107674be89d796e13c8bcae55eb160fdd5a6", "23.09-tf2-py3": "sha256:ddc195f339a7eadc648b0bf17bed974a8d50043616af1c919a2fb8ba2dd0fc2f"}, "filter": ["21*"], "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/tensorflow.
TensorFlow is an open-source software library for high-performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/tensorflow
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/tensorflow:23.09-tf2-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/tensorflow/23.09-tf2-py3
$ module help nvcr.io/nvidia/tensorflow/23.09-tf2-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tensorflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tensorflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tensorflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tensorflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tensorflow

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