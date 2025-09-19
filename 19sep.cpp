class Spreadsheet {
public:
    Spreadsheet(int rows) : spreadSheetGrid(rows+1, vector<int>(26, 0)){
        //spreadSheetGrid = vector<int>(rows, vector<int>(26,0));
    }
    
    void setCell(string cell, int value) {
        int col = cell[0]- 'A';
        int row = stoi(cell.substr(1));
        cout << row << endl;

        setVal(row, col, value);

    }
    void setVal(int r, int c, int v)
    {
        spreadSheetGrid[r][c] = v;
    }

    int getCellVal(int r, int c)
    {
        return spreadSheetGrid[r][c];
    }
    
    void resetCell(string cell) {
        int col = cell[0]- 'A';
        int row = stoi(cell.substr(1));
        setVal(row, col, 0);
    }
    
    int getValue(string formula) 
    {
        string val1, val2, curr;
        int v1= 0, v2=0;
        //bool isVal1Cell = false, isVal2Cell = false;
        int i = 1; //formula[0] is '=' so move to next char
        for(; formula[i] != '+'; curr.push_back(formula[i]), i++);
        i++; // increment to move beyond + sign
        val1 = curr;
        //cout << " val1 = " << val1 <<endl;
        /*curr = "";//reset
        for(; i < formula.size(); i++)
        {
            curr.push_back(formula[i]);
        }*/
        val2 = formula.substr(i);

        //val2 = curr;
        //cout << " val2 = " << val2 <<endl;
        if(val1[0] >= 'A' && val1[0] <= 'Z')
        {
            int col = val1[0]- 'A';
            int row = stoi(val1.substr(1));
            v1 = getCellVal(row, col);
        }
        else
        {
            v1 = stoi(val1);
        }
        if(val2[0] >= 'A' && val2[0] <= 'Z')
        {
            int col = val2[0]- 'A';
            int row = stoi(val2.substr(1));
            v2 = getCellVal(row, col);
        }
        else
        {
            v2 = stoi(val2);
        }

        return v1+v2;
    }

   vector<vector<int>> spreadSheetGrid;
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */
