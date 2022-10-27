---
layout: container
name:  "quay.io/biocontainers/metalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metalign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metalign/container.yaml"
updated_at: "2022-10-27 00:27:59.871249"
latest: "0.12.5--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/metalign"
aliases:
 - "MakeDNADatabase.py"
 - "MakeNodeGraph.py"
 - "MakeStreamingDNADatabase.py"
 - "MakeStreamingPrefilter.py"
 - "QueryDNADatabase.py"
 - "StreamingQueryDNADatabase.py"
 - "StreamingQueryDNADatabase_queue.py"
 - "map_and_profile.py"
 - "metalign.py"
 - "select_db.py"
versions:
 - "0.12.5--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for metalign"
config: {"url": "https://biocontainers.pro/tools/metalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metalign", "latest": {"0.12.5--pyh864c0ab_1": "sha256:42c649b328c0d98d8f6436c7d9071fa4a60191fb094afb4c628e19ba01b54a46"}, "tags": {"0.12.5--pyh864c0ab_1": "sha256:42c649b328c0d98d8f6436c7d9071fa4a60191fb094afb4c628e19ba01b54a46"}, "docker": "quay.io/biocontainers/metalign", "aliases": {"MakeDNADatabase.py": "/usr/local/bin/MakeDNADatabase.py", "MakeNodeGraph.py": "/usr/local/bin/MakeNodeGraph.py", "MakeStreamingDNADatabase.py": "/usr/local/bin/MakeStreamingDNADatabase.py", "MakeStreamingPrefilter.py": "/usr/local/bin/MakeStreamingPrefilter.py", "QueryDNADatabase.py": "/usr/local/bin/QueryDNADatabase.py", "StreamingQueryDNADatabase.py": "/usr/local/bin/StreamingQueryDNADatabase.py", "StreamingQueryDNADatabase_queue.py": "/usr/local/bin/StreamingQueryDNADatabase_queue.py", "map_and_profile.py": "/usr/local/bin/map_and_profile.py", "metalign.py": "/usr/local/bin/metalign.py", "select_db.py": "/usr/local/bin/select_db.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metalign.
shpc-registry automated BioContainers addition for metalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metalign:0.12.5--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metalign/0.12.5--pyh864c0ab_1
$ module help quay.io/biocontainers/metalign/0.12.5--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MakeDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/MakeDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeNodeGraph.py

```bash
$ singularity exec <container> /usr/local/bin/MakeNodeGraph.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeNodeGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeNodeGraph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeStreamingDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/MakeStreamingDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeStreamingDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeStreamingDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MakeStreamingPrefilter.py

```bash
$ singularity exec <container> /usr/local/bin/MakeStreamingPrefilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/MakeStreamingPrefilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MakeStreamingPrefilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### QueryDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/QueryDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/QueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StreamingQueryDNADatabase.py

```bash
$ singularity exec <container> /usr/local/bin/StreamingQueryDNADatabase.py
$ podman run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StreamingQueryDNADatabase_queue.py

```bash
$ singularity exec <container> /usr/local/bin/StreamingQueryDNADatabase_queue.py
$ podman run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase_queue.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StreamingQueryDNADatabase_queue.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_and_profile.py

```bash
$ singularity exec <container> /usr/local/bin/map_and_profile.py
$ podman run --it --rm --entrypoint /usr/local/bin/map_and_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_and_profile.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metalign.py

```bash
$ singularity exec <container> /usr/local/bin/metalign.py
$ podman run --it --rm --entrypoint /usr/local/bin/metalign.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metalign.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_db.py

```bash
$ singularity exec <container> /usr/local/bin/select_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/select_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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