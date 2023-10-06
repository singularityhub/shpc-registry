---
layout: container
name:  "quay.io/biocontainers/viroconstrictor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viroconstrictor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/viroconstrictor/container.yaml"
updated_at: "2023-10-06 03:05:39.839864"
latest: "1.3.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/viroconstrictor"
aliases:
 - "AminoExtract"
 - "ViroConstrictor"
 - "Viroconstrictor"
 - "aminoextract"
 - "directories.py"
 - "markdown-it"
 - "presets.py"
 - "viroConstrictor"
 - "viroconstrictor"
 - "workflow.smk"
 - "mamba-package"
 - "conda2solv"
 - "dumpsolv"
 - "installcheck"
 - "mamba"
 - "mergesolv"
 - "repo2solv"
 - "testsolv"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "tjbench"
 - "conda-env"
 - "cph"
 - "stone"
 - "yte"
 - "plac_runner.py"
 - "docutils"
 - "pulptest"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
versions:
 - "1.2.6--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
 - "1.3.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for viroconstrictor"
config: {"url": "https://biocontainers.pro/tools/viroconstrictor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for viroconstrictor", "latest": {"1.3.1--pyhdfd78af_0": "sha256:7fc849998cd0e7bf6c4ec0f68b40cc5b9a2f77211afc08f306359750bda3e631"}, "tags": {"1.2.6--pyhdfd78af_0": "sha256:ddf08f93f73db8abc301cbe4de578a015d73c3f5e31616f8c9d4d6de1af4e804", "1.3.0--pyhdfd78af_0": "sha256:82359b90e7b7eccc76b46f5d6f9bb86f14fff70fe0ca8bcf0893d3b2f821520d", "1.3.1--pyhdfd78af_0": "sha256:7fc849998cd0e7bf6c4ec0f68b40cc5b9a2f77211afc08f306359750bda3e631"}, "docker": "quay.io/biocontainers/viroconstrictor", "aliases": {"AminoExtract": "/usr/local/bin/AminoExtract", "ViroConstrictor": "/usr/local/bin/ViroConstrictor", "Viroconstrictor": "/usr/local/bin/Viroconstrictor", "aminoextract": "/usr/local/bin/aminoextract", "directories.py": "/usr/local/bin/directories.py", "markdown-it": "/usr/local/bin/markdown-it", "presets.py": "/usr/local/bin/presets.py", "viroConstrictor": "/usr/local/bin/viroConstrictor", "viroconstrictor": "/usr/local/bin/viroconstrictor", "workflow.smk": "/usr/local/bin/workflow.smk", "mamba-package": "/usr/local/bin/mamba-package", "conda2solv": "/usr/local/bin/conda2solv", "dumpsolv": "/usr/local/bin/dumpsolv", "installcheck": "/usr/local/bin/installcheck", "mamba": "/usr/local/bin/mamba", "mergesolv": "/usr/local/bin/mergesolv", "repo2solv": "/usr/local/bin/repo2solv", "testsolv": "/usr/local/bin/testsolv", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "tjbench": "/usr/local/bin/tjbench", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "stone": "/usr/local/bin/stone", "yte": "/usr/local/bin/yte", "plac_runner.py": "/usr/local/bin/plac_runner.py", "docutils": "/usr/local/bin/docutils", "pulptest": "/usr/local/bin/pulptest", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viroconstrictor.
singularity registry hpc automated addition for viroconstrictor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viroconstrictor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viroconstrictor:1.3.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viroconstrictor/1.3.1--pyhdfd78af_0
$ module help quay.io/biocontainers/viroconstrictor/1.3.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viroconstrictor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viroconstrictor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viroconstrictor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viroconstrictor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viroconstrictor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viroconstrictor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AminoExtract

```bash
$ singularity exec <container> /usr/local/bin/AminoExtract
$ podman run --it --rm --entrypoint /usr/local/bin/AminoExtract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AminoExtract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ViroConstrictor

```bash
$ singularity exec <container> /usr/local/bin/ViroConstrictor
$ podman run --it --rm --entrypoint /usr/local/bin/ViroConstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ViroConstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Viroconstrictor

```bash
$ singularity exec <container> /usr/local/bin/Viroconstrictor
$ podman run --it --rm --entrypoint /usr/local/bin/Viroconstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Viroconstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aminoextract

```bash
$ singularity exec <container> /usr/local/bin/aminoextract
$ podman run --it --rm --entrypoint /usr/local/bin/aminoextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aminoextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### directories.py

```bash
$ singularity exec <container> /usr/local/bin/directories.py
$ podman run --it --rm --entrypoint /usr/local/bin/directories.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/directories.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### presets.py

```bash
$ singularity exec <container> /usr/local/bin/presets.py
$ podman run --it --rm --entrypoint /usr/local/bin/presets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/presets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viroConstrictor

```bash
$ singularity exec <container> /usr/local/bin/viroConstrictor
$ podman run --it --rm --entrypoint /usr/local/bin/viroConstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viroConstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viroconstrictor

```bash
$ singularity exec <container> /usr/local/bin/viroconstrictor
$ podman run --it --rm --entrypoint /usr/local/bin/viroconstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viroconstrictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### workflow.smk

```bash
$ singularity exec <container> /usr/local/bin/workflow.smk
$ podman run --it --rm --entrypoint /usr/local/bin/workflow.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/workflow.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda2solv

```bash
$ singularity exec <container> /usr/local/bin/conda2solv
$ podman run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsolv

```bash
$ singularity exec <container> /usr/local/bin/dumpsolv
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installcheck

```bash
$ singularity exec <container> /usr/local/bin/installcheck
$ podman run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba

```bash
$ singularity exec <container> /usr/local/bin/mamba
$ podman run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergesolv

```bash
$ singularity exec <container> /usr/local/bin/mergesolv
$ podman run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repo2solv

```bash
$ singularity exec <container> /usr/local/bin/repo2solv
$ podman run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsolv

```bash
$ singularity exec <container> /usr/local/bin/testsolv
$ podman run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_objective_c_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_objective_c_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_php_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_php_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_python_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_python_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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