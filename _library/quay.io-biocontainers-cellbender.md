---
layout: container
name:  "quay.io/biocontainers/cellbender"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cellbender/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cellbender/container.yaml"
updated_at: "2025-04-07 03:16:48.842846"
latest: "0.3.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cellbender"
aliases:
 - "cellbender"
 - "jupyter-contrib"
 - "jupyter-contrib-nbextension"
 - "jupyter-nbclassic"
 - "jupyter-nbclassic-bundlerextension"
 - "jupyter-nbclassic-extension"
 - "jupyter-nbclassic-serverextension"
 - "jupyter-nbextensions_configurator"
 - "jupyter-server"
 - "loompy"
 - "matplotlib"
 - "qtpy"
 - "jupyter-console"
 - "wsdump"
 - "jupyter-qtconsole"
 - "jupyter-execute"
 - "jupyter-dejavu"
 - "send2trash"
 - "torchrun"
 - "ninja"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
 - "jupyter-serverextension"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "jupyter-notebook"
 - "jupyter-nbconvert"
 - "iptest3"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "iptest"
 - "curve_keygen"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
versions:
 - "0.3.0--pyhdfd78af_0"
 - "0.3.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cellbender"
config: {"url": "https://biocontainers.pro/tools/cellbender", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cellbender", "latest": {"0.3.2--pyhdfd78af_0": "sha256:5eae4a90428e48dddc419a305778eeb6a2472af664ccfb81dffc67d2f8f8ec40"}, "tags": {"0.3.0--pyhdfd78af_0": "sha256:43fe00c046598fd1556434836032bc6e2662533aa63fa494d5cda2ed0422787a", "0.3.2--pyhdfd78af_0": "sha256:5eae4a90428e48dddc419a305778eeb6a2472af664ccfb81dffc67d2f8f8ec40"}, "docker": "quay.io/biocontainers/cellbender", "aliases": {"cellbender": "/usr/local/bin/cellbender", "jupyter-contrib": "/usr/local/bin/jupyter-contrib", "jupyter-contrib-nbextension": "/usr/local/bin/jupyter-contrib-nbextension", "jupyter-nbclassic": "/usr/local/bin/jupyter-nbclassic", "jupyter-nbclassic-bundlerextension": "/usr/local/bin/jupyter-nbclassic-bundlerextension", "jupyter-nbclassic-extension": "/usr/local/bin/jupyter-nbclassic-extension", "jupyter-nbclassic-serverextension": "/usr/local/bin/jupyter-nbclassic-serverextension", "jupyter-nbextensions_configurator": "/usr/local/bin/jupyter-nbextensions_configurator", "jupyter-server": "/usr/local/bin/jupyter-server", "loompy": "/usr/local/bin/loompy", "matplotlib": "/usr/local/bin/matplotlib", "qtpy": "/usr/local/bin/qtpy", "jupyter-console": "/usr/local/bin/jupyter-console", "wsdump": "/usr/local/bin/wsdump", "jupyter-qtconsole": "/usr/local/bin/jupyter-qtconsole", "jupyter-execute": "/usr/local/bin/jupyter-execute", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "send2trash": "/usr/local/bin/send2trash", "torchrun": "/usr/local/bin/torchrun", "ninja": "/usr/local/bin/ninja", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension", "jupyter-serverextension": "/usr/local/bin/jupyter-serverextension", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "jupyter-notebook": "/usr/local/bin/jupyter-notebook", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "iptest3": "/usr/local/bin/iptest3", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "iptest": "/usr/local/bin/iptest", "curve_keygen": "/usr/local/bin/curve_keygen", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cellbender.
singularity registry hpc automated addition for cellbender
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cellbender
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cellbender:0.3.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cellbender/0.3.2--pyhdfd78af_0
$ module help quay.io/biocontainers/cellbender/0.3.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cellbender-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cellbender-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cellbender-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cellbender-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cellbender-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cellbender-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cellbender

```bash
$ singularity exec <container> /usr/local/bin/cellbender
$ podman run --it --rm --entrypoint /usr/local/bin/cellbender   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cellbender   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-contrib

```bash
$ singularity exec <container> /usr/local/bin/jupyter-contrib
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-contrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-contrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-contrib-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-contrib-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-contrib-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-contrib-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic-extension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic-extension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-extension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-extension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbclassic-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbclassic-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbclassic-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextensions_configurator

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextensions_configurator
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextensions_configurator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextensions_configurator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-server

```bash
$ singularity exec <container> /usr/local/bin/jupyter-server
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### loompy

```bash
$ singularity exec <container> /usr/local/bin/loompy
$ podman run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/loompy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matplotlib

```bash
$ singularity exec <container> /usr/local/bin/matplotlib
$ podman run --it --rm --entrypoint /usr/local/bin/matplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtpy

```bash
$ singularity exec <container> /usr/local/bin/qtpy
$ podman run --it --rm --entrypoint /usr/local/bin/qtpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-qtconsole

```bash
$ singularity exec <container> /usr/local/bin/jupyter-qtconsole
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-bundlerextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-bundlerextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-bundlerextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-serverextension

```bash
$ singularity exec <container> /usr/local/bin/jupyter-serverextension
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-serverextension   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-notebook

```bash
$ singularity exec <container> /usr/local/bin/jupyter-notebook
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-notebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest3

```bash
$ singularity exec <container> /usr/local/bin/iptest3
$ podman run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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