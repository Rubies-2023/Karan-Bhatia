const {validationResult} = require('express-validator');
const bcrypt = require('bcryptjs');
const conn = require('../dbConnection').promise();
const fs = require('fs');

// exports.register = async (req, res, next) => {
//     const errors = validationResult(req);
  
//     if (!errors.isEmpty()) {
//       return res.status(422).json({ errors: errors.array() });
//     }
  
//     try {
//       const [row] = await conn.execute(
//         'SELECT `email` FROM `users` WHERE `email`=?',
//         [req.body.email]
//       );
  
//       if (row.length > 0) {
//         return res.status(201).json({
//           message: 'The E-mail already in use',
//         });
//       }
  
//       const hashPass = await bcrypt.hash(req.body.password, 12);
  
//       const [rows] = await conn.execute(
//         'INSERT INTO `users`(`name`,`email`,`password`) VALUES(?,?,?)',
//         [req.body.name, req.body.email, hashPass]
//       );
  
//       if (rows.affectedRows === 1) {
//         const users = [
//           { name: req.body.name, email: req.body.email, password: hashPass },
//         ];
  
//         const jsonData = JSON.stringify(users, null, 2);
  
//         fs.writeFile('users.json', jsonData, (err) => {
//           if (err) {
//             console.error(err);
//             return;
//           }
//           console.log('User data written to file successfully');
//         });
  
//         return res.status(201).json({
//           message: 'The user has been successfully inserted.',
//         });
//       }
//     } catch (err) {
//       next(err);
//     }
//   };
exports.register = async (req, res, next) => {
    const errors = validationResult(req);
  
    if (!errors.isEmpty()) {
      return res.status(422).json({ errors: errors.array() });
    }
  
    try {
      const [row] = await conn.execute(
        'SELECT `email` FROM `users` WHERE `email`=?',
        [req.body.email]
      );
  
      if (row.length > 0) {
        return res.status(201).json({
          message: 'The E-mail already in use',
        });
      }
      const [row1] = await conn.execute(
        'SELECT `name` FROM `users` WHERE `name`=?',
        [req.body.name]
      );
  
      if (row1.length > 0) {
        return res.status(201).json({
          message: 'The Username already in use',
        });
      }
  
      const hashPass = await bcrypt.hash(req.body.password, 12);
  
      const [rows] = await conn.execute(
        'INSERT INTO `users`(`name`,`email`,`password`) VALUES(?,?,?)',
        [req.body.name, req.body.email, hashPass]
      );
  
      if (rows.affectedRows === 1) {
        // read the existing contents of the file
        const rawData = fs.readFileSync('users.json');
        const users = JSON.parse(rawData);
  
        // add the new user to the array
        users.push({
          name: req.body.name,
          email: req.body.email,
          password: hashPass,
        });
  
        // write the updated array back to the file
        const jsonData = JSON.stringify(users, null, 2);
        fs.writeFileSync('users.json', jsonData);
  
        return res.status(201).json({
          message: 'The user has been successfully inserted.',
        });
      }
    } catch (err) {
      next(err);
    }
  };
  