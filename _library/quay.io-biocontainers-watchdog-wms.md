---
layout: container
name:  "quay.io/biocontainers/watchdog-wms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/watchdog-wms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/watchdog-wms/container.yaml"
updated_at: "2024-06-09 03:00:59.738952"
latest: "2.0.8--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/watchdog-wms"
aliases:
 - "watchdog-cmd"
 - "watchdog-configureExamples"
 - "watchdog-createNewModule"
 - "watchdog-dependencyTest"
 - "watchdog-docuTemplateExtractor"
 - "watchdog-downloadModuleMaker"
 - "watchdog-formatCondaYaml"
 - "watchdog-gui"
 - "watchdog-installCondaYaml"
 - "watchdog-moduleTest"
 - "watchdog-moduleValidator"
 - "watchdog-refBookGenerator"
 - "watchdog-reportGenerator"
 - "watchdog-workflowValidator"
 - "basenc"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
 - "chown"
versions:
 - "2.0.8--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for watchdog-wms"
config: {"url": "https://biocontainers.pro/tools/watchdog-wms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for watchdog-wms", "latest": {"2.0.8--hdfd78af_0": "sha256:39b3361ceef1c98c9c837ff3405111f7b2d59f81a7f37e9bc084aaa4b2574590"}, "tags": {"2.0.8--hdfd78af_0": "sha256:39b3361ceef1c98c9c837ff3405111f7b2d59f81a7f37e9bc084aaa4b2574590"}, "docker": "quay.io/biocontainers/watchdog-wms", "aliases": {"watchdog-cmd": "/usr/local/bin/watchdog-cmd", "watchdog-configureExamples": "/usr/local/bin/watchdog-configureExamples", "watchdog-createNewModule": "/usr/local/bin/watchdog-createNewModule", "watchdog-dependencyTest": "/usr/local/bin/watchdog-dependencyTest", "watchdog-docuTemplateExtractor": "/usr/local/bin/watchdog-docuTemplateExtractor", "watchdog-downloadModuleMaker": "/usr/local/bin/watchdog-downloadModuleMaker", "watchdog-formatCondaYaml": "/usr/local/bin/watchdog-formatCondaYaml", "watchdog-gui": "/usr/local/bin/watchdog-gui", "watchdog-installCondaYaml": "/usr/local/bin/watchdog-installCondaYaml", "watchdog-moduleTest": "/usr/local/bin/watchdog-moduleTest", "watchdog-moduleValidator": "/usr/local/bin/watchdog-moduleValidator", "watchdog-refBookGenerator": "/usr/local/bin/watchdog-refBookGenerator", "watchdog-reportGenerator": "/usr/local/bin/watchdog-reportGenerator", "watchdog-workflowValidator": "/usr/local/bin/watchdog-workflowValidator", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/watchdog-wms.
shpc-registry automated BioContainers addition for watchdog-wms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/watchdog-wms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/watchdog-wms:2.0.8--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/watchdog-wms/2.0.8--hdfd78af_0
$ module help quay.io/biocontainers/watchdog-wms/2.0.8--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### watchdog-wms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### watchdog-wms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### watchdog-wms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### watchdog-wms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### watchdog-wms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### watchdog-wms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### watchdog-cmd

```bash
$ singularity exec <container> /usr/local/bin/watchdog-cmd
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-configureExamples

```bash
$ singularity exec <container> /usr/local/bin/watchdog-configureExamples
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-configureExamples   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-configureExamples   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-createNewModule

```bash
$ singularity exec <container> /usr/local/bin/watchdog-createNewModule
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-createNewModule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-createNewModule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-dependencyTest

```bash
$ singularity exec <container> /usr/local/bin/watchdog-dependencyTest
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-dependencyTest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-dependencyTest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-docuTemplateExtractor

```bash
$ singularity exec <container> /usr/local/bin/watchdog-docuTemplateExtractor
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-docuTemplateExtractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-docuTemplateExtractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-downloadModuleMaker

```bash
$ singularity exec <container> /usr/local/bin/watchdog-downloadModuleMaker
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-downloadModuleMaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-downloadModuleMaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-formatCondaYaml

```bash
$ singularity exec <container> /usr/local/bin/watchdog-formatCondaYaml
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-formatCondaYaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-formatCondaYaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-gui

```bash
$ singularity exec <container> /usr/local/bin/watchdog-gui
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-installCondaYaml

```bash
$ singularity exec <container> /usr/local/bin/watchdog-installCondaYaml
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-installCondaYaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-installCondaYaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-moduleTest

```bash
$ singularity exec <container> /usr/local/bin/watchdog-moduleTest
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-moduleTest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-moduleTest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-moduleValidator

```bash
$ singularity exec <container> /usr/local/bin/watchdog-moduleValidator
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-moduleValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-moduleValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-refBookGenerator

```bash
$ singularity exec <container> /usr/local/bin/watchdog-refBookGenerator
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-refBookGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-refBookGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-reportGenerator

```bash
$ singularity exec <container> /usr/local/bin/watchdog-reportGenerator
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-reportGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-reportGenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchdog-workflowValidator

```bash
$ singularity exec <container> /usr/local/bin/watchdog-workflowValidator
$ podman run --it --rm --entrypoint /usr/local/bin/watchdog-workflowValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchdog-workflowValidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chcon

```bash
$ singularity exec <container> /usr/local/bin/chcon
$ podman run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chgrp

```bash
$ singularity exec <container> /usr/local/bin/chgrp
$ podman run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmod

```bash
$ singularity exec <container> /usr/local/bin/chmod
$ podman run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chown

```bash
$ singularity exec <container> /usr/local/bin/chown
$ podman run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
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