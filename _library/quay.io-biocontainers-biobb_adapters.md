---
layout: container
name:  "quay.io/biocontainers/biobb_adapters"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_adapters/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_adapters/container.yaml"
updated_at: "2023-05-23 03:02:41.152691"
latest: "4.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_adapters"
aliases:
 - "bagit.py"
 - "black"
 - "black-primer"
 - "blackd"
 - "jupyter-console"
 - "jupyter-dejavu"
 - "jupyter-qtconsole"
 - "prov-compare"
 - "prov-convert"
 - "send2trash"
 - "cwltool"
 - "schema-salad-doc"
 - "schema-salad-tool"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "jupyter-bundlerextension"
 - "jupyter-nbextension"
versions:
 - "3.7.0--pyhdfd78af_0"
 - "3.8.1--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_adapters"
config: {"url": "https://biocontainers.pro/tools/biobb_adapters", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_adapters", "latest": {"4.0.0--pyhdfd78af_0": "sha256:a412402f3c048173e2b323be4c3672f3d91d2579f96c874e4c702302e3f12d0b"}, "tags": {"3.7.0--pyhdfd78af_0": "sha256:4d8ee7daa23a452321524f2ad7c6f3cadc41bc490670a6d02bfdf03afb990c85", "3.8.1--pyhdfd78af_0": "sha256:471eb904d8c0536eecbe57f48da8360d847981ba5c7f5c9a1499a86c7d88b34d", "4.0.0--pyhdfd78af_0": "sha256:a412402f3c048173e2b323be4c3672f3d91d2579f96c874e4c702302e3f12d0b"}, "docker": "quay.io/biocontainers/biobb_adapters", "aliases": {"bagit.py": "/usr/local/bin/bagit.py", "black": "/usr/local/bin/black", "black-primer": "/usr/local/bin/black-primer", "blackd": "/usr/local/bin/blackd", "jupyter-console": "/usr/local/bin/jupyter-console", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-qtconsole": "/usr/local/bin/jupyter-qtconsole", "prov-compare": "/usr/local/bin/prov-compare", "prov-convert": "/usr/local/bin/prov-convert", "send2trash": "/usr/local/bin/send2trash", "cwltool": "/usr/local/bin/cwltool", "schema-salad-doc": "/usr/local/bin/schema-salad-doc", "schema-salad-tool": "/usr/local/bin/schema-salad-tool", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "jupyter-bundlerextension": "/usr/local/bin/jupyter-bundlerextension", "jupyter-nbextension": "/usr/local/bin/jupyter-nbextension"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_adapters.
shpc-registry automated BioContainers addition for biobb_adapters
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_adapters
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_adapters:4.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_adapters/4.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_adapters/4.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_adapters-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_adapters-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_adapters-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_adapters-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_adapters-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_adapters-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-console

```bash
$ singularity exec <container> /usr/local/bin/jupyter-console
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-qtconsole

```bash
$ singularity exec <container> /usr/local/bin/jupyter-qtconsole
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
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