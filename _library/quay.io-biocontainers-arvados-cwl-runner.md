---
layout: container
name:  "quay.io/biocontainers/arvados-cwl-runner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arvados-cwl-runner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arvados-cwl-runner/container.yaml"
updated_at: "2023-05-06 03:00:44.122438"
latest: "2.0.4--pyh864c0ab_0"
container_url: "https://biocontainers.pro/tools/arvados-cwl-runner"
aliases:
 - "arv-copy"
 - "arv-federation-migrate"
 - "arv-get"
 - "arv-keepdocker"
 - "arv-ls"
 - "arv-migrate-docker19"
 - "arv-normalize"
 - "arv-put"
 - "arv-ws"
 - "arvados-cwl-runner"
 - "bagit.py"
 - "cwl-runner"
 - "prov-compare"
 - "prov-convert"
 - "cwltool"
 - "schema-salad-doc"
 - "schema-salad-tool"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "doesitcache"
 - "coloredlogs"
versions:
 - "2.0.4--pyh864c0ab_0"
description: "shpc-registry automated BioContainers addition for arvados-cwl-runner"
config: {"url": "https://biocontainers.pro/tools/arvados-cwl-runner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arvados-cwl-runner", "latest": {"2.0.4--pyh864c0ab_0": "sha256:a47ea1748a9d708108650476477cf08bf17b03897398b5f9ea3b4348b0caf29d"}, "tags": {"2.0.4--pyh864c0ab_0": "sha256:a47ea1748a9d708108650476477cf08bf17b03897398b5f9ea3b4348b0caf29d"}, "docker": "quay.io/biocontainers/arvados-cwl-runner", "aliases": {"arv-copy": "/usr/local/bin/arv-copy", "arv-federation-migrate": "/usr/local/bin/arv-federation-migrate", "arv-get": "/usr/local/bin/arv-get", "arv-keepdocker": "/usr/local/bin/arv-keepdocker", "arv-ls": "/usr/local/bin/arv-ls", "arv-migrate-docker19": "/usr/local/bin/arv-migrate-docker19", "arv-normalize": "/usr/local/bin/arv-normalize", "arv-put": "/usr/local/bin/arv-put", "arv-ws": "/usr/local/bin/arv-ws", "arvados-cwl-runner": "/usr/local/bin/arvados-cwl-runner", "bagit.py": "/usr/local/bin/bagit.py", "cwl-runner": "/usr/local/bin/cwl-runner", "prov-compare": "/usr/local/bin/prov-compare", "prov-convert": "/usr/local/bin/prov-convert", "cwltool": "/usr/local/bin/cwltool", "schema-salad-doc": "/usr/local/bin/schema-salad-doc", "schema-salad-tool": "/usr/local/bin/schema-salad-tool", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "doesitcache": "/usr/local/bin/doesitcache", "coloredlogs": "/usr/local/bin/coloredlogs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arvados-cwl-runner.
shpc-registry automated BioContainers addition for arvados-cwl-runner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arvados-cwl-runner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arvados-cwl-runner:2.0.4--pyh864c0ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arvados-cwl-runner/2.0.4--pyh864c0ab_0
$ module help quay.io/biocontainers/arvados-cwl-runner/2.0.4--pyh864c0ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arvados-cwl-runner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arvados-cwl-runner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arvados-cwl-runner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arvados-cwl-runner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arvados-cwl-runner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arvados-cwl-runner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arv-copy

```bash
$ singularity exec <container> /usr/local/bin/arv-copy
$ podman run --it --rm --entrypoint /usr/local/bin/arv-copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-federation-migrate

```bash
$ singularity exec <container> /usr/local/bin/arv-federation-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/arv-federation-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-federation-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-get

```bash
$ singularity exec <container> /usr/local/bin/arv-get
$ podman run --it --rm --entrypoint /usr/local/bin/arv-get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-keepdocker

```bash
$ singularity exec <container> /usr/local/bin/arv-keepdocker
$ podman run --it --rm --entrypoint /usr/local/bin/arv-keepdocker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-keepdocker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-ls

```bash
$ singularity exec <container> /usr/local/bin/arv-ls
$ podman run --it --rm --entrypoint /usr/local/bin/arv-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-migrate-docker19

```bash
$ singularity exec <container> /usr/local/bin/arv-migrate-docker19
$ podman run --it --rm --entrypoint /usr/local/bin/arv-migrate-docker19   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-migrate-docker19   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-normalize

```bash
$ singularity exec <container> /usr/local/bin/arv-normalize
$ podman run --it --rm --entrypoint /usr/local/bin/arv-normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-put

```bash
$ singularity exec <container> /usr/local/bin/arv-put
$ podman run --it --rm --entrypoint /usr/local/bin/arv-put   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-put   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-ws

```bash
$ singularity exec <container> /usr/local/bin/arv-ws
$ podman run --it --rm --entrypoint /usr/local/bin/arv-ws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-ws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arvados-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/arvados-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/arvados-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arvados-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prov-compare

```bash
$ singularity exec <container> /usr/local/bin/prov-compare
$ podman run --it --rm --entrypoint /usr/local/bin/prov-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prov-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prov-convert

```bash
$ singularity exec <container> /usr/local/bin/prov-convert
$ podman run --it --rm --entrypoint /usr/local/bin/prov-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prov-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltool

```bash
$ singularity exec <container> /usr/local/bin/cwltool
$ podman run --it --rm --entrypoint /usr/local/bin/cwltool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schema-salad-doc

```bash
$ singularity exec <container> /usr/local/bin/schema-salad-doc
$ podman run --it --rm --entrypoint /usr/local/bin/schema-salad-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schema-salad-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schema-salad-tool

```bash
$ singularity exec <container> /usr/local/bin/schema-salad-tool
$ podman run --it --rm --entrypoint /usr/local/bin/schema-salad-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schema-salad-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdf2dot

```bash
$ singularity exec <container> /usr/local/bin/rdf2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfgraphisomorphism

```bash
$ singularity exec <container> /usr/local/bin/rdfgraphisomorphism
$ podman run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfpipe

```bash
$ singularity exec <container> /usr/local/bin/rdfpipe
$ podman run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfs2dot

```bash
$ singularity exec <container> /usr/local/bin/rdfs2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
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