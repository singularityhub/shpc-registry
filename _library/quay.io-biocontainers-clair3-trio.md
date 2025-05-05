---
layout: container
name:  "quay.io/biocontainers/clair3-trio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clair3-trio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clair3-trio/container.yaml"
updated_at: "2025-05-05 03:20:42.292862"
latest: "0.7--py39hd649744_2"
container_url: "https://biocontainers.pro/tools/clair3-trio"
aliases:
 - "clair3.py"
 - "pypy"
 - "pypy3"
 - "pypy3.6"
 - "run_clair3_trio.sh"
 - "whatshap"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "estimator_ckpt_converter"
 - "google-oauthlib-tool"
 - "igzip"
 - "tf_upgrade_v2"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
 - "toco_from_protos"
 - "vcf_sample_filter.py"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "tensorboard"
 - "vcf_filter.py"
 - "vcf_melt"
 - "pigz"
 - "unpigz"
 - "env_parallel"
versions:
 - "0.3--py36hb9dc472_1"
 - "0.3--py36hb9dc472_2"
 - "0.5--py36hb9dc472_0"
 - "0.6--py39hb9dc472_0"
 - "0.6--py39h8492097_1"
 - "0.7--py39hf5e1c6e_0"
 - "0.7--py39h46983ab_1"
 - "0.7--py39hd649744_2"
description: "singularity registry hpc automated addition for clair3-trio"
config: {"url": "https://biocontainers.pro/tools/clair3-trio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for clair3-trio", "latest": {"0.7--py39hd649744_2": "sha256:ef31f8f31bc17b7709d9df89d57845f5648059fce4c68f9459f887d32c597976"}, "tags": {"0.3--py36hb9dc472_1": "sha256:8fbba669b4cfead32d76807dff1485569364b99def76664cf8c5efdedd00547e", "0.3--py36hb9dc472_2": "sha256:686ef253d602b4c1c9dbd52bcc5127f7ec08096d012baa9af971295b52ba19f5", "0.5--py36hb9dc472_0": "sha256:6c85e073ea22a767cc581088f9ffb814b5acdc99a4f1d47144e9efbaa44b71d2", "0.6--py39hb9dc472_0": "sha256:b27b724b79affd26b49afd2c3e2d5e88995b881b6b7cbbfd4098e0c909365240", "0.6--py39h8492097_1": "sha256:d4829450032e8d1d487af61936b46ce040f9ae27ad722248614e1af618760f42", "0.7--py39hf5e1c6e_0": "sha256:2ae685fe5e38063e451873a1eff55839afa8728ec1b39cb9155964b938450359", "0.7--py39h46983ab_1": "sha256:b9df6887e12d8cab06cc1f403fc2c4cb6b441140e883cc4db3fcd9087fec89a9", "0.7--py39hd649744_2": "sha256:ef31f8f31bc17b7709d9df89d57845f5648059fce4c68f9459f887d32c597976"}, "docker": "quay.io/biocontainers/clair3-trio", "aliases": {"clair3.py": "/usr/local/bin/clair3.py", "pypy": "/usr/local/bin/pypy", "pypy3": "/usr/local/bin/pypy3", "pypy3.6": "/usr/local/bin/pypy3.6", "run_clair3_trio.sh": "/usr/local/bin/run_clair3_trio.sh", "whatshap": "/usr/local/bin/whatshap", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "igzip": "/usr/local/bin/igzip", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco", "toco_from_protos": "/usr/local/bin/toco_from_protos", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "tensorboard": "/usr/local/bin/tensorboard", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "env_parallel": "/usr/local/bin/env_parallel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clair3-trio.
singularity registry hpc automated addition for clair3-trio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clair3-trio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clair3-trio:0.7--py39hd649744_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clair3-trio/0.7--py39hd649744_2
$ module help quay.io/biocontainers/clair3-trio/0.7--py39hd649744_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clair3-trio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clair3-trio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clair3-trio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clair3-trio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clair3-trio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clair3-trio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clair3.py

```bash
$ singularity exec <container> /usr/local/bin/clair3.py
$ podman run --it --rm --entrypoint /usr/local/bin/clair3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clair3.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy

```bash
$ singularity exec <container> /usr/local/bin/pypy
$ podman run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3

```bash
$ singularity exec <container> /usr/local/bin/pypy3
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3.6

```bash
$ singularity exec <container> /usr/local/bin/pypy3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_clair3_trio.sh

```bash
$ singularity exec <container> /usr/local/bin/run_clair3_trio.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_clair3_trio.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_clair3_trio.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_dump

```bash
$ singularity exec <container> /usr/local/bin/gdbm_dump
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_load

```bash
$ singularity exec <container> /usr/local/bin/gdbm_load
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbmtool

```bash
$ singularity exec <container> /usr/local/bin/gdbmtool
$ podman run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimator_ckpt_converter

```bash
$ singularity exec <container> /usr/local/bin/estimator_ckpt_converter
$ podman run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tflite_convert

```bash
$ singularity exec <container> /usr/local/bin/tflite_convert
$ podman run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saved_model_cli

```bash
$ singularity exec <container> /usr/local/bin/saved_model_cli
$ podman run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco

```bash
$ singularity exec <container> /usr/local/bin/toco
$ podman run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco_from_protos

```bash
$ singularity exec <container> /usr/local/bin/toco_from_protos
$ podman run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tensorboard

```bash
$ singularity exec <container> /usr/local/bin/tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
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