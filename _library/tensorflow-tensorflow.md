---
layout: container
name:  "tensorflow/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/tensorflow/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/tensorflow/tensorflow/container.yaml"
updated_at: "2024-02-01 03:01:31.919842"
latest: "2.15.0rc1"
container_url: "https://hub.docker.com/r/tensorflow/tensorflow"
aliases:
 - "python"
versions:
 - "2.5.0-custom-op-gpu-ubuntu16"
 - "2.5.0rc0-gpu-jupyter"
 - "2.6.0"
 - "2.6.0rc0-gpu-jupyter"
 - "2.7.0"
 - "2.7.0rc0"
 - "2.8.0"
 - "2.8.0rc0"
 - "latest-gpu"
 - "2.7.1-gpu"
 - "2.7.1"
 - "2.6.1"
 - "2.5.1"
 - "2.9.0rc1"
 - "2.9.1"
 - "2.8.2"
 - "2.7.3"
 - "2.10.0rc2"
 - "2.10.0rc3"
 - "2.10.0"
 - "2.9.2"
 - "2.8.3"
 - "2.7.4"
 - "2.11.0rc2"
 - "2.11.0"
 - "2.10.1"
 - "2.9.3"
 - "2.8.4"
 - "2.12.0rc0"
 - "2.12.0"
 - "2.11.1"
 - "2.13.0rc1"
 - "2.13.0"
 - "2.14.0rc1"
 - "2.14.0"
 - "2.15.0rc1"
 - "2.15.0"
description: "An end-to-end open source platform for machine learning."
config: {"docker": "tensorflow/tensorflow", "url": "https://hub.docker.com/r/tensorflow/tensorflow", "maintainer": "@vsoch", "description": "An end-to-end open source platform for machine learning.", "latest": {"2.15.0rc1": "sha256:224cac1c9371f104bdf3e9318301c09ec7270403bea23a54cbd317810038740e"}, "tags": {"2.5.0-custom-op-gpu-ubuntu16": "sha256:478bee6f0691b48d74adc3fcffe3e9ececf35df5c02860cc51a2c48b1d92c730", "2.5.0rc0-gpu-jupyter": "sha256:9808e04142b09482bb6b3d1738430ae7472a214dd38e086d41e481b376fa9abd", "2.6.0": "sha256:773d5ce09e4ce003db02740c6a372a8a9f43be2bac23544d8f452bfec5347c53", "2.6.0rc0-gpu-jupyter": "sha256:358b5bf90aaf4e56813ff22f2981d86fab7ddc59552b0be6022ae04d6a9f43c3", "2.7.0": "sha256:31e09cf438a41f12c759cc8cc79c6b0fbb0db5abfc3de8169e916c8c9ac38dc5", "2.7.0rc0": "sha256:abbc457c9b7c0725d7d0db885dbb313db3d0ae25733b083900a508efb672af94", "2.8.0": "sha256:7c01f75d58fadc2cd1109d5baac1925ed131e05925d840b1b49363c794d1c4db", "2.8.0rc0": "sha256:11e5d21a786da523d2f7de530c083d5c72a06e02c8895c84595d107c579027a1", "latest-gpu": "sha256:dc97d4feec5dee719a74afe25ff041242a8f1d379c15d690c33e1e9ebe828c07", "2.7.1-gpu": "sha256:581575fc3a736398f0dff9e950f57f2e6d808296267ac98325451a0b1d101dd0", "2.7.1": "sha256:c9940aa904694a1e5dc4ad3add3c933de45091d5b48e37e94993f19d1d213205", "2.6.1": "sha256:8f343633898c500138979065b62ecb50be4a29f8e7adfadd8f0b168d2642eab1", "2.5.1": "sha256:07d837eced57184599f50944a47e10a23584dae666dc93aa9a762b1111651fa7", "2.9.0rc1": "sha256:2faf5970c62fb58bb6a5281bc5467d82bc6765fe0572cc72ccbca78f50d9e0be", "2.9.1": "sha256:a5c8c8995f16c63a9dbb59e586bed2e15dbf1024ac08065aaaad053c5173f83e", "2.8.2": "sha256:5abc48f6a1ccdf73f052fa60939583f96ead8b3a4f33c0ac5ccf1baf13d12786", "2.7.3": "sha256:be6652df4285e5c1781bccc1dea53a0290e380373ba53f8edb41092a4478dc06", "2.10.0rc2": "sha256:f6f27fbcb9f6c6888c96dc2320358830f51278e1210a81aa0f525ae5437df0f3", "2.10.0rc3": "sha256:60f2ff58e65a4e648ffd61ea94455eb1e4331eb88d0927d0344d84970325394d", "2.10.0": "sha256:7f9f23ce2473eb52d17fe1b465c79c3a3604047343e23acc036296f512071bc9", "2.9.2": "sha256:26dca0f464d1d47543ad588efd37c77e59ee95ceca9639077a3db79a35f42632", "2.8.3": "sha256:721c113dcf7473224705035f81c0f320bbd72ef451310fd5f79fafd097f681c8", "2.7.4": "sha256:6edc0e345b2e87af2a41815296fcebda2f3f35ecd4494809218c9afd907f1a78", "2.11.0rc2": "sha256:38030e31a2a4a8b5ef45c4b4afe8b7c355f12f983ddab57291248bea5f90830c", "2.11.0": "sha256:eea5989852623037f354c49404b66761467516b79ab7af26e643b5ac7382c53f", "2.10.1": "sha256:b633084418ec697b275d6cee7da679a76bf8626bfb18188d6a44cdce3482047f", "2.9.3": "sha256:cc93ae477033b20faad24576be5884b17f45eda033a98a3bb8a219790dcef862", "2.8.4": "sha256:932d8676f71b5536c0b3346d4f43cb22bfa400978f8552f250cea63b65b6022d", "2.12.0rc0": "sha256:c4ba8ce589d8651eae169ac6ca33e595e119a2ec626086cf09ce5577db88f95c", "2.12.0": "sha256:7263b3490857fedad7f71ad219518358b0341ee5c716a47d4691daddc47cad3b", "2.11.1": "sha256:0d6a5e2c3b144c18f2e389563dc052b0c0e2f040c911ed8851c59d9e9c930f36", "2.13.0rc1": "sha256:8b8ff16509a5921d3d2a55da004c77266c43f31959b2ad897ba64ee463c7158d", "2.13.0": "sha256:f133c99eba6e59b921ea7543c81417cd831c9983f5d6ce65dff7adb0ec79d830", "2.14.0rc1": "sha256:bfd89366919f5490a77f0da3f53087913725cf9dc4a6a47bde86748df8c75858", "2.14.0": "sha256:e39bbda78194ea735df765d6f15396d9a08354319af156ffec4ad2c6eeba469b", "2.15.0rc1": "sha256:224cac1c9371f104bdf3e9318301c09ec7270403bea23a54cbd317810038740e", "2.15.0": "sha256:4689c724a7d65a7d289cc2ae536fa3cd6b636b2df3e23da3a44ffdd6ac3af46f"}, "filter": ["2[.]*"], "features": {"gpu": true}, "aliases": {"python": "/usr/local/bin/python"}}
---

This module is a singularity container wrapper for tensorflow/tensorflow.
An end-to-end open source platform for machine learning.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install tensorflow/tensorflow
```

Or a specific version:

```bash
$ shpc install tensorflow/tensorflow:2.15.0rc1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load tensorflow/tensorflow/2.15.0rc1
$ module help tensorflow/tensorflow/2.15.0rc1
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


#### python

```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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