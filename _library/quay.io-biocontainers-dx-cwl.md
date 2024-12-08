---
layout: container
name:  "quay.io/biocontainers/dx-cwl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dx-cwl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dx-cwl/container.yaml"
updated_at: "2024-12-08 03:12:30.896830"
latest: "0.1.0a20180905--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/dx-cwl"
aliases:
 - "bagit.py"
 - "dx"
 - "dx-app-wizard"
 - "dx-build-app"
 - "dx-build-applet"
 - "dx-clone-asset"
 - "dx-cwl"
 - "dx-docker"
 - "dx-download-all-inputs"
 - "dx-fetch-bundled-depends"
 - "dx-generate-dxapp"
 - "dx-jobutil-add-output"
 - "dx-jobutil-dxlink"
 - "dx-jobutil-new-job"
 - "dx-jobutil-parse-link"
 - "dx-jobutil-report-error"
 - "dx-log-stream"
 - "dx-mount-all-inputs"
 - "dx-notebook-reconnect"
 - "dx-print-bash-vars"
 - "dx-upload-all-outputs"
 - "prov-compare"
 - "prov-convert"
 - "wsdump.py"
 - "xattr"
 - "cwltool"
 - "schema-salad-doc"
 - "schema-salad-tool"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "doesitcache"
 - "activate-global-python-argcomplete"
versions:
 - "0.1.0a20180905--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for dx-cwl"
config: {"url": "https://biocontainers.pro/tools/dx-cwl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dx-cwl", "latest": {"0.1.0a20180905--hdfd78af_3": "sha256:929bad76310739ea3799f1ac58bcfd540defc93e18a043b35a25c15031f2c2d4"}, "tags": {"0.1.0a20180905--hdfd78af_3": "sha256:929bad76310739ea3799f1ac58bcfd540defc93e18a043b35a25c15031f2c2d4"}, "docker": "quay.io/biocontainers/dx-cwl", "aliases": {"bagit.py": "/usr/local/bin/bagit.py", "dx": "/usr/local/bin/dx", "dx-app-wizard": "/usr/local/bin/dx-app-wizard", "dx-build-app": "/usr/local/bin/dx-build-app", "dx-build-applet": "/usr/local/bin/dx-build-applet", "dx-clone-asset": "/usr/local/bin/dx-clone-asset", "dx-cwl": "/usr/local/bin/dx-cwl", "dx-docker": "/usr/local/bin/dx-docker", "dx-download-all-inputs": "/usr/local/bin/dx-download-all-inputs", "dx-fetch-bundled-depends": "/usr/local/bin/dx-fetch-bundled-depends", "dx-generate-dxapp": "/usr/local/bin/dx-generate-dxapp", "dx-jobutil-add-output": "/usr/local/bin/dx-jobutil-add-output", "dx-jobutil-dxlink": "/usr/local/bin/dx-jobutil-dxlink", "dx-jobutil-new-job": "/usr/local/bin/dx-jobutil-new-job", "dx-jobutil-parse-link": "/usr/local/bin/dx-jobutil-parse-link", "dx-jobutil-report-error": "/usr/local/bin/dx-jobutil-report-error", "dx-log-stream": "/usr/local/bin/dx-log-stream", "dx-mount-all-inputs": "/usr/local/bin/dx-mount-all-inputs", "dx-notebook-reconnect": "/usr/local/bin/dx-notebook-reconnect", "dx-print-bash-vars": "/usr/local/bin/dx-print-bash-vars", "dx-upload-all-outputs": "/usr/local/bin/dx-upload-all-outputs", "prov-compare": "/usr/local/bin/prov-compare", "prov-convert": "/usr/local/bin/prov-convert", "wsdump.py": "/usr/local/bin/wsdump.py", "xattr": "/usr/local/bin/xattr", "cwltool": "/usr/local/bin/cwltool", "schema-salad-doc": "/usr/local/bin/schema-salad-doc", "schema-salad-tool": "/usr/local/bin/schema-salad-tool", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "doesitcache": "/usr/local/bin/doesitcache", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dx-cwl.
shpc-registry automated BioContainers addition for dx-cwl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dx-cwl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dx-cwl:0.1.0a20180905--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dx-cwl/0.1.0a20180905--hdfd78af_3
$ module help quay.io/biocontainers/dx-cwl/0.1.0a20180905--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dx-cwl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dx-cwl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dx-cwl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dx-cwl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dx-cwl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dx-cwl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx

```bash
$ singularity exec <container> /usr/local/bin/dx
$ podman run --it --rm --entrypoint /usr/local/bin/dx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-app-wizard

```bash
$ singularity exec <container> /usr/local/bin/dx-app-wizard
$ podman run --it --rm --entrypoint /usr/local/bin/dx-app-wizard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-app-wizard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-build-app

```bash
$ singularity exec <container> /usr/local/bin/dx-build-app
$ podman run --it --rm --entrypoint /usr/local/bin/dx-build-app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-build-app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-build-applet

```bash
$ singularity exec <container> /usr/local/bin/dx-build-applet
$ podman run --it --rm --entrypoint /usr/local/bin/dx-build-applet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-build-applet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-clone-asset

```bash
$ singularity exec <container> /usr/local/bin/dx-clone-asset
$ podman run --it --rm --entrypoint /usr/local/bin/dx-clone-asset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-clone-asset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-cwl

```bash
$ singularity exec <container> /usr/local/bin/dx-cwl
$ podman run --it --rm --entrypoint /usr/local/bin/dx-cwl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-cwl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-docker

```bash
$ singularity exec <container> /usr/local/bin/dx-docker
$ podman run --it --rm --entrypoint /usr/local/bin/dx-docker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-docker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-download-all-inputs

```bash
$ singularity exec <container> /usr/local/bin/dx-download-all-inputs
$ podman run --it --rm --entrypoint /usr/local/bin/dx-download-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-download-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-fetch-bundled-depends

```bash
$ singularity exec <container> /usr/local/bin/dx-fetch-bundled-depends
$ podman run --it --rm --entrypoint /usr/local/bin/dx-fetch-bundled-depends   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-fetch-bundled-depends   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-generate-dxapp

```bash
$ singularity exec <container> /usr/local/bin/dx-generate-dxapp
$ podman run --it --rm --entrypoint /usr/local/bin/dx-generate-dxapp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-generate-dxapp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-add-output

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-add-output
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-add-output   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-add-output   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-dxlink

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-dxlink
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-dxlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-dxlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-new-job

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-new-job
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-new-job   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-new-job   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-parse-link

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-parse-link
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-parse-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-parse-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-report-error

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-report-error
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-report-error   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-report-error   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-log-stream

```bash
$ singularity exec <container> /usr/local/bin/dx-log-stream
$ podman run --it --rm --entrypoint /usr/local/bin/dx-log-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-log-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-mount-all-inputs

```bash
$ singularity exec <container> /usr/local/bin/dx-mount-all-inputs
$ podman run --it --rm --entrypoint /usr/local/bin/dx-mount-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-mount-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-notebook-reconnect

```bash
$ singularity exec <container> /usr/local/bin/dx-notebook-reconnect
$ podman run --it --rm --entrypoint /usr/local/bin/dx-notebook-reconnect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-notebook-reconnect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-print-bash-vars

```bash
$ singularity exec <container> /usr/local/bin/dx-print-bash-vars
$ podman run --it --rm --entrypoint /usr/local/bin/dx-print-bash-vars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-print-bash-vars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-upload-all-outputs

```bash
$ singularity exec <container> /usr/local/bin/dx-upload-all-outputs
$ podman run --it --rm --entrypoint /usr/local/bin/dx-upload-all-outputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-upload-all-outputs   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### wsdump.py

```bash
$ singularity exec <container> /usr/local/bin/wsdump.py
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xattr

```bash
$ singularity exec <container> /usr/local/bin/xattr
$ podman run --it --rm --entrypoint /usr/local/bin/xattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xattr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
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