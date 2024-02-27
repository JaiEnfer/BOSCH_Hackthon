#!/bin/bash

# Install necessary dependencies
pip install pandas scikit-learn

# Copy Python files and CSV data
cp gui.py recommendation_engine.py material_properties.csv /path/to/installation/directory

# Create executable script
echo '#!/bin/bash' > material_recommendation_system.sh
echo 'python3 /path/to/installation/directory/gui.py' >> material_recommendation_system.sh
chmod +x material_recommendation_system.sh

echo "Material Recommendation System has been installed. Run 'material_recommendation_system.sh' to start the application."
