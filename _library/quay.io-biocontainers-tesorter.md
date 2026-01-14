---
layout: container
name:  "quay.io/biocontainers/tesorter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tesorter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tesorter/container.yaml"
updated_at: "2026-01-14 04:31:46.353051"
latest: "1.5.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tesorter"
aliases:
 - "LTR_retriever.py"
 - "RepeatMasker.py"
 - "TEsorter"
 - "TEsorter-test"
 - "concatenate_domains.py"
 - "get_record.py"
 - "ppserver.py"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
 - "readme.pdf"
versions:
 - "1.3.0--py_0"
 - "1.4.6--pyhdfd78af_0"
 - "1.4.6--pyhdfd78af_1"
 - "1.4.7--pyhdfd78af_0"
 - "1.4.7--pyhdfd78af_1"
 - "1.5.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for tesorter"
config: {"url": "https://biocontainers.pro/tools/tesorter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tesorter", "latest": {"1.5.1--pyhdfd78af_0": "sha256:25b9878a395bb1b6c4143726b1c8e1dc4ea7799d130e9a0e22858f0e3d61eba3"}, "tags": {"1.3.0--py_0": "sha256:9cdc74b9e07458e3e4a57a3e15faa45137cb748b31a39f40cbfc9e200bc27788", "1.4.6--pyhdfd78af_0": "sha256:65a6a909483f9a405a7fa5106ea409c981cfb09eee545b6916b54e9347f95081", "1.4.6--pyhdfd78af_1": "sha256:36afd35dc05702670756b6c6007fa86465c265601ddf9375fc12618a45002c4f", "1.4.7--pyhdfd78af_0": "sha256:29f996fc932412686e7eb4cc194a5162ca96cacf2041a36093f0f233f7c73cb7", "1.4.7--pyhdfd78af_1": "sha256:b0d0fe492641e536b2ca080344ed3174a5891841063e3a007c02af3a850180bf", "1.5.1--pyhdfd78af_0": "sha256:25b9878a395bb1b6c4143726b1c8e1dc4ea7799d130e9a0e22858f0e3d61eba3"}, "docker": "quay.io/biocontainers/tesorter", "aliases": {"LTR_retriever.py": "/usr/local/bin/LTR_retriever.py", "RepeatMasker.py": "/usr/local/bin/RepeatMasker.py", "TEsorter": "/usr/local/bin/TEsorter", "TEsorter-test": "/usr/local/bin/TEsorter-test", "concatenate_domains.py": "/usr/local/bin/concatenate_domains.py", "get_record.py": "/usr/local/bin/get_record.py", "ppserver.py": "/usr/local/bin/ppserver.py", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect", "readme.pdf": "/usr/local/bin/readme.pdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tesorter.
shpc-registry automated BioContainers addition for tesorter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tesorter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tesorter:1.5.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tesorter/1.5.1--pyhdfd78af_0
$ module help quay.io/biocontainers/tesorter/1.5.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tesorter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tesorter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tesorter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tesorter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tesorter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tesorter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LTR_retriever.py

```bash
$ singularity exec <container> /usr/local/bin/LTR_retriever.py
$ podman run --it --rm --entrypoint /usr/local/bin/LTR_retriever.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LTR_retriever.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepeatMasker.py

```bash
$ singularity exec <container> /usr/local/bin/RepeatMasker.py
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatMasker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatMasker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TEsorter

```bash
$ singularity exec <container> /usr/local/bin/TEsorter
$ podman run --it --rm --entrypoint /usr/local/bin/TEsorter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEsorter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TEsorter-test

```bash
$ singularity exec <container> /usr/local/bin/TEsorter-test
$ podman run --it --rm --entrypoint /usr/local/bin/TEsorter-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEsorter-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concatenate_domains.py

```bash
$ singularity exec <container> /usr/local/bin/concatenate_domains.py
$ podman run --it --rm --entrypoint /usr/local/bin/concatenate_domains.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concatenate_domains.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_record.py

```bash
$ singularity exec <container> /usr/local/bin/get_record.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_record.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_record.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppserver.py

```bash
$ singularity exec <container> /usr/local/bin/ppserver.py
$ podman run --it --rm --entrypoint /usr/local/bin/ppserver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppserver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readme.pdf

```bash
$ singularity exec <container> /usr/local/bin/readme.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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