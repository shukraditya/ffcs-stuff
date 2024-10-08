import json
import itertools


#slot mapped with it's timing
slot_timings = {
    "A1": [("Monday", "0800-0850"), ("Wednesday", "0900-0950")],
    "TA1": [("Friday", "1000-1050")],
    "TAA1": [("Tuesday", "1200-1250")],
    "B1": [("Tuesday", "0800-0850"), ("Thursday", "0900-0950")],
    "TB1": [("Monday", "1100-1150")],
    "C1": [("Wednesday", "0800-0850"), ("Friday", "0900-0950")],
    "TC1": [("Tuesday", "1100-1150")],
    "TCC1": [("Thursday", "1200-1250")],
    "D1": [("Thursday", "0800-0850"), ("Monday", "1000-1050")],
    "TD1": [("Friday", "1200-1250")],
    "E1": [("Friday", "0800-0850"), ("Tuesday", "1000-1050")],
    "TE1": [("Thursday", "1100-1150")],
    "F1": [("Monday", "0900-0950"), ("Wednesday", "1000-1050")],
    "TF1": [("Friday", "1100-1150")],
    "G1": [("Tuesday", "0900-0950"), ("Thursday", "1000-1050")],
    "TG1": [("Monday", "1200-1250")],
    "A2": [("Monday", "1400-1450"), ("Wednesday", "1500-1550")],
    "F2": [("Monday", "1500-1550"), ("Wednesday", "1600-1650")],
    "D2": [("Monday", "1600-1650"), ("Thursday", "1400-1450")],
    "TB2": [("Monday", "1700-1750")],
    "TG2": [("Monday", "1800-1850")],
    "B2": [("Tuesday", "1400-1450"), ("Thursday", "1500-1550")],
    "G2": [("Tuesday", "1500-1550"), ("Thursday", "1600-1650")],
    "E2": [("Tuesday", "1600-1650"), ("Friday", "1400-1450")],
    "TC2": [("Tuesday", "1700-1750")],
    "TAA2": [("Tuesday", "1800-1850")],
    "C2": [("Wednesday", "1400-1450"), ("Friday", "1500-1550")],
    "TD2": [("Wednesday", "1700-1750")],
    "TBB2": [("Wednesday", "1800-1850")],
    "TE2": [("Thursday", "1700-1750")],
    "TCC2": [("Thursday", "1800-1850")],
    "TA2": [("Friday", "1600-1650")],
    "TF2": [("Friday", "1700-1750")],
    "TDD2": [("Friday", "1800-1850")],
    "L1+L2": [("Monday", "0800-0940")],
    "L3+L4": [("Monday", "0950-1130")],
    "L5+L6": [("Monday", "1140-1230")],
    "L7+L8": [("Tuesday", "0800-0940")],
    "L9+L10": [("Tuesday", "0950-1130")],
    "L11+L12": [("Tuesday", "1140-1230")],
    "L13+L14": [("Wednesday", "0800-0940")],
    "L15+L16": [("Wednesday", "0950-1130")],
    "L17+L18": [("Wednesday", "1140-1230")],
    "L19+L20": [("Thursday", "0800-0940")],
    "L21+L22": [("Thursday", "0950-1130")],
    "L23+L24": [("Thursday", "1140-1230")],
    "L25+L26": [("Friday", "0800-0940")],
    "L27+L28": [("Friday", "0950-1130")],
    "L29+L30": [("Friday", "1140-1230")],
    "L31+L32": [("Monday", "1400-1540")],
    "L33+L34": [("Monday", "1550-1730")],
    "L35+L36": [("Monday", "1830-1920")],
    "L37+L38": [("Tuesday", "1400-1540")],
    "L39+L40": [("Tuesday", "1550-1730")],
    "L41+L42": [("Tuesday", "1800-1920")],
    "L43+L44": [("Wednesday", "1400-1540")],
    "L45+L46": [("Wednesday", "1550-1730")],
    "L47+L48": [("Wednesday", "1740-1920")],
    "L49+L50": [("Thursday", "1400-1540")],
    "L51+L52": [("Thursday", "1550-1730")],
    "L53+L54": [("Thursday", "1740-1920")],
    "L55+L56": [("Friday", "1400-1540")],
    "L57+L58": [("Friday", "1550-1730")],
    "L59+L60": [("Friday", "1740-1920")],
    "V1": [("Wednesday", "1100-1150")],
    # Add any additional slots if necessary
}

#input json
input_data = '''
{
  "courses": [
    {
      "title": "Front End Design and Testing",
      "code": "CSI3029",
      "slots": [
        {
          "prof": "Arulkumar V",
          "slots": "C1,C2,L15+L16,L35+L36"
        },
        {
          "prof": "Dhinakaran N",
          "slots": "C2,L1+L2"
        }
      ]
    },
    {
      "title": "Application Development and Deployment Architecture",
      "code": "CSI3025",
      "slots": [
        {
          "prof": "Sudhakar P",
          "slots": "B1,B2,L1+L2,L55+L56"
        }
      ]
    },
    {
      "title": "Artificial Intelligence and Expert Systems",
      "code": "CSI3003",
      "slots": [
        {
          "prof": "Tamizharasi T",
          "slots": "G1+TG1"
        },
        {
          "prof": "Madhan E S",
          "slots": "G1+TG1"
        },
        {
          "prof": "Sathya K",
          "slots": "G1+TG1"
        },
        {
          "prof": "Jeevanantham A.K.",
          "slots": "G2+TG2"
        },
        {
          "prof": "Siva Sankari S",
          "slots": "G2+TG2"
        },
        {
          "prof": "Yuvaraj N",
          "slots": "G1+TG1"
        },
        {
          "prof": "Sivakumar V",
          "slots": "G2+TG2"
        },
        {
          "prof": "Ganesh Shamrao Khekare",
          "slots": "G2+TG2"
        }
      ]
    },
    {
      "title": "Applied Cryptography and Network Security",
      "code": "CSI3002",
      "slots": [
        {
          "prof": "Nivitha K",
          "slots": "A1,A2,L11+L12,L41+L42"
        },
        {
          "prof": "Thangaramya K",
          "slots": "A1,A2,L25+L26,L51+L52"
        },
        {
          "prof": "S M Farooq",
          "slots": "A1,A2,L7+L8,L51+L52"
        },
        {
          "prof": "Sunil Kumar",
          "slots": "A1,A2,L11+L12,L41+L42"
        }
      ]
    },
    {
      "title": "Cloud Computing and methodologies",
      "code": "CSI3001",
      "slots": [
        {
          "prof": "Dhivyaa CR",
          "slots": "B1+TB1,B2+TB2,L27+L28.L43+L44"
        },
        {
          "prof": "Muthunagai",
          "slots": "B1+TB1,B2+TB2,L13+L14,L43+L44"
        },
        {
          "prof": "Ranjithkumar S",
          "slots": "B1+TB1,B2+TB2,L27+L28,L53+L54"
        },
        {
          "prof": "Pushpa Gothwal",
          "slots": "B1+TB1,B2+TB2,L13+L14,L59+L60"
        }
      ]
    },
    {
      "title": "Data Science Programming",
      "code": "CSI3004",
      "slots": [
        {
          "prof": "Ganesh Shamrao Khekare",
          "slots": "C1,C2,L21+L22,L31+L32"
        },
        {
          "prof": "Meenakshi SP",
          "slots": "C1,C2,L21+L22,L31+L32"
        }
      ]
    },
    {
      "title": "Advanced Computer Architecture",
      "code": "CSI3021",
      "slots": [
        {
          "prof": "Thirunavukkarasan M",
          "slots": "E1+TE1"
        },
        {
          "prof": "Sreethar S",
          "slots": "E1+TE1"
        },
        {
          "prof": "Narmalli Jayakrishna",
          "slots": "E1+TE1"
        },
        {
          "prof": "Suresh A",
          "slots": "E1+TE1"
        },
        {
          "prof": "Krishnaraj N",
          "slots": "E2+TE2"
        },
        {
          "prof": "Deepa D",
          "slots": "E2+TE2"
        },
        {
          "prof": "Pushpa Gothwal",
          "slots": "E2+TE2"
        },
        {
          "prof": "Latha Reddy N",
          "slots": "E2+TE2"
        }
      ]
    },
    {
      "title": "Japanese for Beginners",
      "code": "JAP1001",
      "slots": [
        {
          "prof": "Khanjan",
          "slots": "B1"
        },
        {
          "prof": "Hiya Mukherjee",
          "slots": "C1"
        }
      ]
    },
    {
      "title": "Intelligent Database Systems",
      "code": "MDI3004",
      "slots": [
        {
          "prof": "Deepika J",
          "slots": "G1+TG1"
        },
        {
          "prof": "Thangaramya K",
          "slots": "G1+TG1"
        },
        {
          "prof": "Saurabh Agrawal",
          "slots": "G2+TG2"
        },
        {
          "prof": "Jeevanajyothi Pujari",
          "slots": "G2+TG2"
        }
      ]
    },
    {
      "title": "Getting Started to Skill Enhancemnets",
      "code": "STS3021",
      "slots": [
        {
          "prof": "Ethnus",
          "slots": "D1+TD1,D2+TD2"
        },
        {
          "prof": "Face",
          "slots": "D1+TD1,D2+TD2"
        }
      ]
    },
    {
      "title": "Logic and Combanitorics for Computer Science",
      "code": "CSI4002",
      "slots": [
        {
          "prof": "Bhawana Tyagi",
          "slots": "F1+TF1"
        },
        {
          "prof": "Somasundaram SK",
          "slots": "F1+TF1"
        },
        {
          "prof": "Uma Priya D",
          "slots": "F1+TF1"
        },
        {
          "prof": "Rohini S",
          "slots": "F1+TF1"
        },
        {
          "prof": "Nivethitha k",
          "slots": "F2+TF2"
        },
        {
          "prof": "Dinesh R",
          "slots": "F2+TF2"
        },
        {
          "prof": "Malini S",
          "slots": "F2+TF2"
        },
        {
          "prof": "Pavithra M",
          "slots": "F2+TF2"
        }
      ]
    }
  ]
}
'''

data = json.loads(input_data)

courses = []
for course in data['courses']:
    course_code = course['code']
    slot_options = []
    for slot_option in course['slots']:
        prof = slot_option['prof']
        slots = slot_option['slots'].split(',')
        slot_options.append({
            'prof': prof,
            'slots': slots,
        })
    courses.append({
        'code': course_code,
        'slot_options': slot_options
    })


course_slot_options = [course['slot_options'] for course in courses]
all_combinations = list(itertools.product(*course_slot_options))

print(course_slot_options)

print(len(all_combinations))