---
layout: container
name:  "quay.io/biocontainers/hmftools-linx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-linx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-linx/container.yaml"
updated_at: "2023-05-18 04:56:18.724341"
latest: "1.22.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-linx"
aliases:
 - "croco-0.6-config"
 - "csslint-0.6"
 - "linx"
 - "x86_64-conda_cos6-linux-gnu-pkg-config"
 - "circos"
 - "circos.exe"
 - "compile.bat"
 - "compile.make"
 - "gddiag"
 - "list.modules"
 - "test.modules"
 - "g-ir-doc-tool"
 - "giffilter"
 - "gifsponge"
versions:
 - "1.7--0"
 - "1.21--hdfd78af_0"
 - "1.20--hdfd78af_0"
 - "1.19--hdfd78af_0"
 - "1.18--hdfd78af_0"
 - "1.17--hdfd78af_0"
 - "1.22--hdfd78af_0"
 - "1.22.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmftools-linx"
config: {"url": "https://biocontainers.pro/tools/hmftools-linx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-linx", "latest": {"1.22.1--hdfd78af_0": "sha256:02fbf02b9c6dc03ced20f828f83df32c4080f4e7313f889117f01317a855db0a"}, "tags": {"1.7--0": "sha256:96ad73788663f0f2576719e7f8f0c415bad6211cbec5685168f00a966b87b4b9", "1.21--hdfd78af_0": "sha256:ec48aca10f2f993fc9056c90c36a4ff1f134b0fa296b20989bc641e139a65dff", "1.20--hdfd78af_0": "sha256:c541d2c20af026c0c801fd86ed1ff2b7af6523faf382d12d3cf9fae81c200c20", "1.19--hdfd78af_0": "sha256:5a399b69c147eef6bf46c15ddd13e907c6017109488189703b9c8b37b8cbf75c", "1.18--hdfd78af_0": "sha256:8fdd0a01b4667499f6f289c91dc7eaf0664e3d55e43caf78a7cec5d8d47bcfe0", "1.17--hdfd78af_0": "sha256:6e6a7be19fb1878261e708f269468f234f74916613cf0f4f52ab7a36e83eadfa", "1.22--hdfd78af_0": "sha256:93d4f68994967e6a8d38db0468a20fd0b8de7874452e14547b34844f4102f205", "1.22.1--hdfd78af_0": "sha256:02fbf02b9c6dc03ced20f828f83df32c4080f4e7313f889117f01317a855db0a"}, "docker": "quay.io/biocontainers/hmftools-linx", "aliases": {"croco-0.6-config": "/usr/local/bin/croco-0.6-config", "csslint-0.6": "/usr/local/bin/csslint-0.6", "linx": "/usr/local/bin/linx", "x86_64-conda_cos6-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config", "circos": "/usr/local/bin/circos", "circos.exe": "/usr/local/bin/circos.exe", "compile.bat": "/usr/local/bin/compile.bat", "compile.make": "/usr/local/bin/compile.make", "gddiag": "/usr/local/bin/gddiag", "list.modules": "/usr/local/bin/list.modules", "test.modules": "/usr/local/bin/test.modules", "g-ir-doc-tool": "/usr/local/bin/g-ir-doc-tool", "giffilter": "/usr/local/bin/giffilter", "gifsponge": "/usr/local/bin/gifsponge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-linx.
shpc-registry automated BioContainers addition for hmftools-linx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-linx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-linx:1.22.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-linx/1.22.1--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-linx/1.22.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-linx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-linx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-linx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-linx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-linx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-linx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### croco-0.6-config

```bash
$ singularity exec <container> /usr/local/bin/croco-0.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csslint-0.6

```bash
$ singularity exec <container> /usr/local/bin/csslint-0.6
$ podman run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linx

```bash
$ singularity exec <container> /usr/local/bin/linx
$ podman run --it --rm --entrypoint /usr/local/bin/linx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos6-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos

```bash
$ singularity exec <container> /usr/local/bin/circos
$ podman run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circos.exe

```bash
$ singularity exec <container> /usr/local/bin/circos.exe
$ podman run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circos.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.bat

```bash
$ singularity exec <container> /usr/local/bin/compile.bat
$ podman run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile.make

```bash
$ singularity exec <container> /usr/local/bin/compile.make
$ podman run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile.make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gddiag

```bash
$ singularity exec <container> /usr/local/bin/gddiag
$ podman run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gddiag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list.modules

```bash
$ singularity exec <container> /usr/local/bin/list.modules
$ podman run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.modules

```bash
$ singularity exec <container> /usr/local/bin/test.modules
$ podman run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-doc-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-doc-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifsponge

```bash
$ singularity exec <container> /usr/local/bin/gifsponge
$ podman run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
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