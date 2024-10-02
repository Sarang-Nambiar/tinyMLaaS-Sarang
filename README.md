# Interview task: [Full Stack Developer for TinyMLaaS Platform](https://github.com/njlabo/share/blob/main/job-post-tinymlaas.md#full-stack-developer-for-tinymlaas-platform)

## Instruction
This is an interview task. You don't need to get everything done. At latest please come back in a week.
- Convert a CLI program, `run` into a `Web service`.
  - This CLI program predicts a number from `0` to `9` from a handwriting digits image, [MNIST](https://en.wikipedia.org/wiki/MNIST_database).
- Implement a backend server with [fastAPI](https://fastapi.tiangolo.com/).
- Implement a frontend server with [Streamlit](https://streamlit.io/) or [stlite](https://github.com/whitphx/stlite) as serverless.
  1. Upload a MNIST image.
  2. Predict its number.
  3. Show an `image` and the `bar chart` of each numbers' probability.
- Implement all in [docker-compose](https://docs.docker.com/compose/).
  
## WoW
- Try to use [GH Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) for [TDD](https://www.agilealliance.org/glossary/tdd/).
  - [AppTest: a faster way to build quality Streamlit](https://blog.streamlit.io/apptest-faster-automated-testing/)
- Try to create feature branches (ref. [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)).
- Send `Pull-Request` (PR) occasionally.
  - Be kind to a reviewer to understand your changes easily from PR / commit logs.
- Ask any questions via PR or Issue comments as communication.
- Please don't share this task to anyone ;)
- We'll have a follow-up session to discuss solutions at the end.

## Bonus
Not maodatory at all but please consider the following since you need them in our development.
- TDD
- [GitHub workfow](https://docs.github.com/en/actions/using-workflows) for CI/CD.
- [docker-in-docker](https://shisho.dev/blog/posts/docker-in-docker/) within `docker-compose`.
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/)
- [stlite](https://github.com/whitphx/stlite) as serverless streamlit.
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) to manage features.
