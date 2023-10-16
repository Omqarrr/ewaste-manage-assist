[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue)](https://developer.ibm.com/callforcode/solutions/projects/get-started/)

# E-Waste Manage Assist/ Waste Warriors

- [E-Waste Manage Assist/ Waste Warriors](#e-waste-manage-assist-waste-warriors)
  - [Project summary](#project-summary)
    - [Revolutionizing e-waste management using solution based out of generative AI](#revolutionizing-e-waste-management-using-solution-based-out-of-generative-ai)
    - [How our technology solution can help](#how-our-technology-solution-can-help)
    - [Our idea](#our-idea)
  - [Technology implementation](#technology-implementation)
    - [IBM AI service(s) used](#ibm-ai-services-used)
    - [Other IBM technology used](#other-ibm-technology-used)
    - [Solution architecture](#solution-architecture)
  - [Presentation materials](#presentation-materials)
    - [Solution demo video](#solution-demo-video)
    - [Project development roadmap](#project-development-roadmap)
  - [Additional details](#additional-details)
    - [How to run the project](#how-to-run-the-project)
    - [Live demo](#live-demo)
  - [About this template](#about-this-template)
    - [Contributing](#contributing)
    - [Versioning](#versioning)
    - [Authors](#authors)
    - [License](#license)
    - [Acknowledgments](#acknowledgments)

_INSTRUCTIONS: Complete all required deliverable sections below._

## Project summary

### Revolutionizing e-waste management using solution based out of generative AI

Within factory environments, eliminating the need for human intervention and reducing the risk of hazardous exposure.
Our solution harnesses Generative AI to automate the process, enabling robots to accurately classify and segregate e-waste.
Simultaneously gathering data to predict and manage future e-waste generation, thereby promoting workplace safety and environmental sustainability.

### How our technology solution can help

- Public Awareness about Health Hazards of E-waste.
- Predict Future E-waste Generation.
- Reduce risk of human exposure to e-waste by automating e-waste material segregation.

### Our idea

The global issue of electronic waste, or e-waste, poses significant environmental and health risks. As the proliferation of electronic devices continues, responsible e-waste management is of paramount importance. In response to this challenge, we have developed a groundbreaking solution that combines the power of Generative AI to serve three critical purposes:

**1. Generating Awareness through AI-Generated Advertisements:**
The first facet of our solution focuses on generating awareness about e-waste management among the general public. Electronic waste contains hazardous materials that, when improperly disposed of, can harm the environment and human health. Our AI-driven system creates tailored and impactful advertisements to educate the public on the importance of recycling and responsible e-waste disposal. By harnessing Generative AI, these advertisements can be customized to target specific audiences, making the message more relatable and engaging.

**2. Data Collection and Validation for Predictive Insights:**
The second aspect of our solution involves capturing data from various public sources online and validating this data to gain insights into future e-waste generation trends. Accurate data is crucial for developing sustainable waste management strategies. Our system aggregates data from sources such as government reports, industry publications, and public databases. It then employs advanced data validation techniques to ensure the information's reliability and accuracy. This validated data is analyzed to predict and understand the future trajectory of e-waste generation, helping organizations and policymakers make informed decisions regarding e-waste management and resource allocation.

**3. Factory E-Waste Segregation with Robotic Assistance:**
The third and most innovative component of our solution is the application of Generative AI in factory environments to automate the segregation of e-waste, eliminating the need for human intervention. Robots equipped with AI-driven systems are deployed to classify and sort e-waste items efficiently. These robots can identify and categorize different electronic components with exceptional precision, streamlining the sorting process. Once sorted, the e-waste is placed in specific racks for further processing or recycling. This automated system enhances workplace safety by reducing human exposure to hazardous materials, while also increasing operational efficiency in managing e-waste within the factory environment.

**How the Three Components Work Together:**
The synergy between these three components is what makes our solution truly remarkable. The awareness generated through AI-driven advertisements not only educates the public but also promotes responsible e-waste disposal practices. Concurrently, the data collected and validated from public sources helps organizations anticipate the scale of e-waste challenges they will face. This predictive insight allows for better planning and resource allocation, ensuring that e-waste is managed efficiently. 

In factory environments, the AI-powered robotic segregation system takes this a step further by automating the sorting process, reducing the risk to human workers and increasing efficiency. The data-driven approach also extends to factory operations, where the system can track the types and quantities of e-waste processed, helping organizations better manage their e-waste streams and make informed decisions on recycling and disposal methods.

**Conclusion:**
Our triple-purpose solution is a comprehensive and forward-thinking approach to e-waste management. By combining Generative AI to raise awareness, collect and validate data for predictive insights, and automate e-waste segregation in factory settings, we address the e-waste challenge at various levels. Our goal is to create a more sustainable and responsible approach to electronic waste management that benefits the environment, public health, and the global community as a whole. With this integrated approach, we aim to pave the way for a greener, cleaner, and safer future for all.

More detail is available in our [description document](./docs/DESCRIPTION.md).

## Technology implementation

### IBM AI service(s) used

_INSTRUCTIONS: Included here is a list of commonly used IBM AI services. Remove any services you did not use, or add others from the linked catalog not already listed here. Leave only those included in your solution code. Provide details on where and how you used each IBM AI service to help judges review your implementation. Remove these instructions._

- [IBM Natural Language Understanding](https://cloud.ibm.com/catalog/services/natural-language-understanding) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Discovery](https://cloud.ibm.com/catalog/services/watson-discovery) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Speech to Text](https://cloud.ibm.com/catalog/services/speech-to-text) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- [Watson Text to Speech](https://cloud.ibm.com/catalog/services/text-to-speech) - WHERE AND HOW THIS IS USED IN OUR SOLUTION
- List any additional [IBM AI services](https://cloud.ibm.com/catalog?category=ai#services) used or remove this line

### Other IBM technology used

INSTRUCTIONS: List any other IBM technology used in your solution and describe how each component was used. If you can provide links to/details on exactly where these were used in your code, that would help the judges review your submission.

### Solution architecture

Diagram and step-by-step description of the flow of our solution:

![Video transcription/translaftion app](https://developer.ibm.com/developer/tutorials/cfc-starter-kit-speech-to-text-app-example/images/cfc-covid19-remote-education-diagram-2.png)

1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Presentation materials

_INSTRUCTIONS: The following deliverables should be officially posted to your My Team > Submissions section of the [Call for Code Global Challenge resources site](https://cfc-prod.skillsnetwork.site/), but you can also include them here for completeness. Replace the examples seen here with your own deliverable links._

### Solution demo video

[![Watch the video](https://raw.githubusercontent.com/Liquid-Prep/Liquid-Prep/main/images/readme/IBM-interview-video-image.png)](https://youtu.be/vOgCOoy_Bx0)

### Project development roadmap

The project currently does the following things.

- Feature 1
- Feature 2
- Feature 3

In the future we plan to...

See below for our proposed schedule on next steps after Call for Code 2023 submission.

![Roadmap](./images/roadmap.jpg)

## Additional details

_INSTRUCTIONS: The following deliverables are suggested, but **optional**. Additional details like this can help the judges better review your solution. Remove any sections you are not using._

### How to run the project

INSTRUCTIONS: In this section you add the instructions to run your project on your local machine for development and testing purposes. You can also add instructions on how to deploy the project in production.

### Live demo

You can find a running system to test at...

See our [description document](./docs/DESCRIPTION.md) for log in credentials.

---

_INSTRUCTIONS: You can remove the below section from your specific project README._

## About this template

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

### Authors

<a href="https://github.com/Call-for-Code/Project-Sample/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Call-for-Code/Project-Sample" />
</a>

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

### License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Based on [Billie Thompson's README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
