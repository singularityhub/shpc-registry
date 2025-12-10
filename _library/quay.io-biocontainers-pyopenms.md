---
layout: container
name:  "quay.io/biocontainers/pyopenms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyopenms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyopenms/container.yaml"
updated_at: "2025-12-10 03:47:23.315214"
latest: "3.4.1--py310h7ad0250_2"
container_url: "https://biocontainers.pro/tools/pyopenms"
aliases:
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
versions:
 - "2.8.0--py36h24c8720_1"
 - "2.9.1--py39h4b47abe_0"
 - "2.9.1--py310h4b47abe_1"
 - "2.9.1--py311h9b8898c_3"
 - "3.0.0--py39h9b8898c_0"
 - "3.1.0--py310h9b8898c_0"
 - "3.1.0--py311h9b8898c_0"
 - "3.0.0--py310h9b8898c_0"
 - "2.9.1--py39h9b8898c_3"
 - "2.8.0--py38hd8d5640_1"
 - "3.2.0--py312h714e36f_1"
 - "3.3.0--py39h85de438_5"
 - "3.4.1--py311he9bd0e4_0"
 - "3.4.1--py310h7ad0250_2"
description: "shpc-registry automated BioContainers addition for pyopenms"
config: {"url": "https://biocontainers.pro/tools/pyopenms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyopenms", "latest": {"3.4.1--py310h7ad0250_2": "sha256:7af2d762d79bb75650920a0c0b6d8fec3b0a2ea5fa57a73890264be6bc87690d"}, "tags": {"2.8.0--py36h24c8720_1": "sha256:dd0c6357466b8d2930ed748e66174ce5a24b7dfead9e241e780f1b348003485c", "2.9.1--py39h4b47abe_0": "sha256:21f3bb3bfa0368c6e1583fd6b2d48100651c4424a8d94ff234bf6947485097d0", "2.9.1--py310h4b47abe_1": "sha256:a9c9e6f171db0a3065bf1c51d0d771d42778981b47d5b201aba9491c3f79120a", "2.9.1--py311h9b8898c_3": "sha256:c4541e5d30dfc0a67d73358816ecfa29070aadcd1685ec1a6a1824a01a3feb1b", "3.0.0--py39h9b8898c_0": "sha256:88a9d45b1262eec8bbdad8e16fbe16da188781474bf0b6c38e8e361158f845a4", "3.1.0--py310h9b8898c_0": "sha256:71a657b4c4d0a611dc226ea5ac280bf82298344bb2f979175b5d233e58890e19", "3.1.0--py311h9b8898c_0": "sha256:a6d54c4c74f22f0e2107740c4ded5150363941264a4ae5f87d5703224b1eabdc", "3.0.0--py310h9b8898c_0": "sha256:e8fa43947e0ad858a226d4491eca870ff4c5a1a62c80e327bf694a42ec585ad1", "2.9.1--py39h9b8898c_3": "sha256:5f6520fd707c5032137770220fb72c0e2ea3500ed6aeb68f7a9d19c116392d15", "2.8.0--py38hd8d5640_1": "sha256:52898ff11afbd6c84995c9a705187d39e9dc604b407c976c47ad3b01252f2b6b", "3.2.0--py312h714e36f_1": "sha256:d49c0ecd729bb4173802f084701458eb85d7f5f04870c2d8b1afa61db6686a83", "3.3.0--py39h85de438_5": "sha256:489a507291f6f5006ba0a74b00b331243f71de7c908b27169388de5043a85836", "3.4.1--py311he9bd0e4_0": "sha256:c41451d5bb8a36f28c85bcf262f8e40b6c2f6d050f25f31ca083ea869d4501ad", "3.4.1--py310h7ad0250_2": "sha256:7af2d762d79bb75650920a0c0b6d8fec3b0a2ea5fa57a73890264be6bc87690d"}, "docker": "quay.io/biocontainers/pyopenms", "aliases": {"svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyopenms.
shpc-registry automated BioContainers addition for pyopenms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyopenms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyopenms:3.4.1--py310h7ad0250_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyopenms/3.4.1--py310h7ad0250_2
$ module help quay.io/biocontainers/pyopenms/3.4.1--py310h7ad0250_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyopenms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyopenms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyopenms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyopenms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyopenms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyopenms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /usr/local/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /usr/local/bin/DOMCount
$ podman run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /usr/local/bin/DOMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /usr/local/bin/EnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /usr/local/bin/MemParse
$ podman run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /usr/local/bin/PParse
$ podman run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /usr/local/bin/PSVIWriter
$ podman run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
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